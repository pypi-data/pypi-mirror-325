#!/usr/bin/env python
# Copyright listfs authors. Distributed under GPL-3.0-or-later
"""listfs. Mount file listings as a FUSE filesystem.
Usage:
  listfs [-o MOUNT_OPTIONS] [--foreground]
         ([--skip-components=N] [--prefix-dir=DIR] LISTING)...
         MOUNTPOINT
  listfs -h | --help | --help-formats | --version

Arguments:
  LISTING              Path to a listing file.
                       Must be in a supported format.
                       May be compressed with zstd, gzip, bzip2, lz4, or xz.
                       See --help-formats for supported formats.
  MOUNTPOINT           Directory where the filesystem will be mounted.

Options:
  -o --options         FUSE mount options.
  --foreground         Do not fork to background.
  --skip-components=N  Skip the first N components of the path.
                       Affects the next LISTING argument.
  --prefix-dir=DIR     Prefix the path with DIR.
                       Affects the next LISTING argument.
  -h --help            Show this message and exit.
  --help-formats       Show supported listing format detail and exit.
  --version            Show the version and exit.
"""
__version__ = "0.6.1"

import atexit
import bz2
import errno
import faulthandler
import gc
import grp
import gzip
import io
import json
import logging
import lzma
import math
import os
import pwd
import re
import signal
import stat
import sys
import textwrap
from collections import defaultdict, OrderedDict
from contextlib import contextmanager
from dataclasses import dataclass, asdict
from datetime import datetime
from itertools import islice
from time import perf_counter
from typing import Sequence, Dict, List, Tuple

import pyfuse3
import trio
import zstandard as zstd
from lz4.frame import LZ4FrameFile
from pyfuse3 import InodeT, FileNameT, FileHandleT

short_usage = """Usage: listfs [OPTIONS] ([--skip-components=N] [--prefix-dir=DIR] LISTING)... MOUNTPOINT
Usage: listfs --help"""
format_help = """Each supported format has one record per line.
Listings may be compressed with zstd, gzip, bzip2, lz4, or xz.

Supported formats:
* basic lines of paths
* `find -ls` listing
* `tar -c -vv` listing
* tabular text: mtime bytes path
* jsonl: ["mtime", bytes, "path"]
* jsonl: ["mtime", bytes, blocks_1k, "path"]
* jsonl: {"t":"mtime", "m":"mode", "s":bytes, "p":"path"}

---
basic lines of paths
One path per line, parsed literally.
Example listing:
/Documents/
/Documents/linux_iso_links.txt

---
`find -ls` listing
Listing of files as created by `find -ls`.
Example command: `find ./dir -ls | tee -a listing.txt`
Example output:
  13 0 drwxr-sr-x 2  user user    13 Dec 11  2024 ./dir
1005 4 -rw-r--r-- 1  user user  4096 Jan 15 19:20 ./dir/file.txt
   | | || links___|     | | bytes__| |__mtime___| |__path
   | | ||_perms         | |_group
   | | |__type          |___user
   | |____1KiB blocks
   |______inode

---
`tar -c -vv` listing
Listing of files as created by `tar -cvv`.
The `--full-time` tar argument is supported.
Example command: `tar -c -vv --index-file=listing.log -f /dev/nst0 ./dir`
Example output:
drwxr-xr-x  root/root       0 2024-08-05 12:10 ./dir/
-rw-r--r--* root/root  102400 2025-01-02 02:12 ./dir/file.txt
||_perms  | | group_| bytes_| |_mtime________| |_path
|__type   | |_user
          |___xattr, selinux, and acl data indicator

---
tabular text listing
Listing of files with whitespace-separated mtime, bytes, and a literal path.
If the path ends with a slash, it is assumed to be a directory.
Filenames with newlines are not supported in this format.
Each record is treated as only either a regular file or a directory.
    If a directory does not end with a slash,
    then listfs will treat it as directory
    when it finds the directory contents.
Example listing:
1732859280.5934580927       0   Documents/
1732859284.2913177150   24334   Documents/file.txt
|_mtime with decimal    |_bytes |_path

---
jsonl (array) listing
One JSON array per line.
A variant structured form of the tabular text listing.
The array may have 3 or 4 items, with the blocks field as optional:
* mtime timestamp string, in seconds with optional decimal
* size in bytes
* size in 1KiB blocks (optional)
* path (assumed to be a directory if ending with "/", otherwise assumed to be a file)
Example listing (3 items):
["1732859280.5934580927", 0, "Documents/"]
["1732859284.2913177150", 24334, "Documents/file.txt"]
Example listing (4 items):
["1732859280.5934580927", 0, 0, "Documents/"]
["1732859284.2913177150", 24334, 24, "Documents/file.txt"]

---
jsonl (object) listing
One JSON object per line. Only the "p" path field is required.
Fields:
* "t": mtime timestamp string, in seconds with optional decimal
* "y": file type; "d" for directory, "f" for file, "l" for symlink
* "i": original inode
* "e": `1` if empty, `0` otherwise
* "m": octal file mode string, e.g. "0644"
* "s": size in bytes
* "k": size in 1KiB blocks
* "p": path
Example listing:
{"t":"1732859280.5934580927","y":"d","i":5121024,"e":0,"m":"0755","s":1024,"k":1,"p":"/docs"}
{"t":"1722859284.2913177150","y":"f","i":5121337,"e":0,"m":"0644","s":4096,"k":4,"p":"/docs/file.txt"}
{"p":"/docs/file2.txt"}
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
total_line_count = 0

# crw-r--r--  root/root       1,5 2024-09-17 15:47 zero
# drw-r--r--  user/user         0 2024-09-17 15:47 code/
# -rw-r--r--  user/user       120 2024-09-17 15:47 code/README.md
# 12        3 4    5        6 7 8 9                10
# 1: type, 2: perms, 3: xattrs?, 4: user, 5: group, 6: size, 7: major, 8: minor, 9: mtime, 10: path
#
gnu_tar_format_re = re.compile(r"^([-dlhsbc])([rwxsStT-]{9})([ .+*]?)\s+([^/]*)/(\w+)\s+(?:(\d+)|(\d+),(\d+))\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}(?::[\d.]+)?)\s+(.*)")
# field 3 possible values:
# * (nothing): --xattrs, --selinux, --acls were not used
# * " ": one of the flags were used, but no data present
# * "*": --xattrs used and data present
# * ".": --selinux used and data present
# * "+": --acls used and data present
# Note: tar -c -vvv --xattrs format writes xattrs, selinux, and acls on separate lines.
#       Possible low-priority future feature.
# Aside: macOS / bsdtar uses "?" and "@" to denote xattr presence in the
#        output of `ls`, but does not use these symbols in tar or find.

# 1681475278.2696418010   24334   /Documents/data.txt
tabular_format_re = re.compile(r"^(\d+(?:.?\d+)?)\s+(\d+)\s+(.*)$")
# 5627106      76 -rw-r--r-- 1 user user 74677       Jan  9 14:16 Documents/screenshot.png
#      41       4 drwxr-sr-x 1 user  100 1376        Feb 11  2024 ISOs/recovery
#   20055 2740608 -rwxr-xr-x 1 user user 2806382592  Dec 15 19:20 ISOs/recovery/Fedora-KDE-Live-x86_64-41-1.4.iso
# 1       2       3   4      5     6    7     8      9            10
# inode   blocks  typ perms  links user group size   date         path
find_ls_format_re = re.compile(r"^\s*(\d+)\s+(\d+)\s+([-dlhsbc])([rwxsStT-]{9})\s+(\d+)\s+(\S+)\s+(\S+)\s+(?:(\d+)|(\d+),\s*(\d+))\s+(\S+\s+\S+\s+\S+)\s+(.*)$")


filetype_to_mode = {  # @see: findutils/find/print.c mode_to_filetype
    "f": stat.S_IFREG,   # regular file
    "d": stat.S_IFDIR,   # directory
    "l": stat.S_IFLNK,   # symbolic link
    "s": stat.S_IFSOCK,  # Unix domain socket
    "b": stat.S_IFBLK,   # block device
    "c": stat.S_IFCHR,   # character device
    "p": stat.S_IFIFO,   # FIFO
    "D": stat.S_IFDOOR,  # Door (e.g. on Solaris)
    "U": stat.S_IFREG,   # Unknown */ # fallback to regular file

    # symlink error types:
    "N": stat.S_IFLNK,  # ENOENT and ENOTDIR
    "L": stat.S_IFLNK,  # ELOOP
    "?": stat.S_IFLNK,  # unknown

    # tar listing types: @see tar/src/list.c:1153 simple_print_header
    "-": stat.S_IFREG,  # ls -l format for regular file
    "h": stat.S_IFREG,  # tar format for hard link to previously archived file
                        # "hrw-r--r-- [...] myfile1.txt link to myfile2.txt"
}


def file_type_to_string(st_mode):
    """Take st_mode / octal number and return the file type."""
    if stat.S_ISREG(st_mode):
        return "Regular file"
    elif stat.S_ISDIR(st_mode):
        return "Directory"
    elif stat.S_ISLNK(st_mode):
        return "Symbolic link"
    elif stat.S_ISSOCK(st_mode):
        return "Socket"
    elif stat.S_ISBLK(st_mode):
        return "Block device"
    elif stat.S_ISCHR(st_mode):
        return "Character device"
    elif stat.S_ISFIFO(st_mode):
        return "FIFO/pipe"
    elif stat.S_ISDOOR(st_mode):
        return "Door"
    elif stat.S_ISPORT(st_mode):
        return "Event port"
    elif stat.S_ISWHT(st_mode):
        return "Whiteout"
    else:
        return "Unknown file type"


def fileperm_to_mode(perm):
    """Take rwxrwxrwx permission string and return the mode."""
    # Opposite of fileperm(). @see cpython/Modules/_stat.c:412 fileperm(mode_t mode, char *buf)
    if len(perm) != 9:
        raise ValueError(f"permission string must be 9 characters long: {perm}")
    mode = 0
    if perm[0] == "r":
        mode |= stat.S_IRUSR
    if perm[1] == "w":
        mode |= stat.S_IWUSR
    if perm[2] == "s":
        mode |= stat.S_ISUID | stat.S_IXUSR
    if perm[2] == "S":
        mode |= stat.S_ISUID
    if perm[2] == "x":
        mode |= stat.S_IXUSR
    if perm[3] == "r":
        mode |= stat.S_IRGRP
    if perm[4] == "w":
        mode |= stat.S_IWGRP
    if perm[5] == "s":
        mode |= stat.S_ISGID | stat.S_IXGRP
    if perm[5] == "S":
        mode |= stat.S_ISGID
    if perm[5] == "x":
        mode |= stat.S_IXGRP
    if perm[6] == "r":
        mode |= stat.S_IROTH
    if perm[7] == "w":
        mode |= stat.S_IWOTH
    if perm[8] == "t":
        mode |= stat.S_ISVTX | stat.S_IXOTH
    if perm[8] == "T":
        mode |= stat.S_ISVTX
    if perm[8] == "x":
        mode |= stat.S_IXOTH
    return mode


escape_chars = {
    "a": "\a",
    "b": "\b",
    "f": "\f",
    "n": "\n",
    "r": "\r",
    "t": "\t",
    "v": "\v",
    "\\": "\\",

    # Below is only for locale quoting style,
    # but should be fine for escape quoting style too
    " ": " ",
    '"': '"',
}


def is_octal(c: str):
    return all("0" <= c <= "7" for c in c)


def unquote_gnulib(arg: str):
    # @see gnulib/lib/quotearg.c quotearg and quotearg_buffer_restyled
    # My tar defaults to --quoting-style=escape
    # Do not use unicode_escape - it mangles non ascii text
    # Bad: path = codecs.decode(path, "unicode_escape", "surrogateescape")
    # Also @see findutils/find/print.c parse_escape_char
    # Also @see findutils/lib/printquoted.c print_quoted

    # find defaults to locale_quoting_style, which is different from escape_quoting_style

    # TODO improve the performance. This is very slow.
    # 126000 records per second when this is not used,
    # 98000 records per second when this is used.
    result = []
    b = bytearray()
    i = 0
    while i < len(arg):
        if arg[i] == "\\":
            if i + 1 < len(arg) and (c := escape_chars.get(arg[i + 1])):
                result.append(arg[:i] + c)
                arg = arg[i + 2:]
                i = 0
                continue
            while i + 3 < len(arg) and is_octal(arg[i + 1:i + 4]):
                if i > 0:
                    result.append(arg[:i])
                b.append(int(arg[i + 1:i + 4], 8))
                arg = arg[i + 4:]
                i = 0
            if b:
                result.append(b.decode())
                b.clear()
                continue
            # Expected escape but sequence not handled
            # Treat as literal
        i += 1
    result.append(arg)
    return "".join(result)


def parse_ls_date(date_str: str, assumed_year: int):
    """
    Parses a date string in either of these formats:
    - "Feb 11  2024" (with a year)
    - "Dec 15 19:20" (without a year, includes only time)

    Returns a datetime object.
    """
    try:
        if ":" not in date_str:
            # Try parsing with the format that includes a year
            parsed_date = datetime.strptime(date_str, "%b %d %Y")
            return parsed_date
    except ValueError:
        pass
    # If parsing fails, fallback to the format without a year and assume the default year
    parsed_date = datetime.strptime(f"{date_str};{assumed_year}", "%b %d %H:%M;%Y")
    while parsed_date > datetime.now():
        assumed_year -= 1
        parsed_date = datetime.strptime(f"{date_str};{assumed_year}", "%b %d %H:%M;%Y")
    return parsed_date


@contextmanager
def open_maybe_compressed(filepath, mode):
    """
    Open a file handle for compressed or plain text files based on magic numbers.
    Supports paths that represent special files like `/dev/stdin`.
    <mode> can be "rt" or "rb", for text or binary.
    """

    if mode not in {"rt", "rb"}:
        raise ValueError("Mode must be either 'rt' or 'rb'")

    raw_stream = None
    buffered_stream = None
    reader = None

    try:
        # Open as binary to detect the magic number
        raw_stream = open(filepath, "rb")
        buffered_stream = io.BufferedReader(raw_stream)

        magic = buffered_stream.peek(8)

        encoding = "utf-8" if mode == "rt" else None
        errors = "ignore" if mode == "rt" else None

        # Decide the type of compression
        if magic.startswith(b"\x1f\x8b"):  # gzip
            reader = gzip.open(
                buffered_stream,
                mode=mode,
                encoding=encoding,
                errors=errors,
            )
        elif magic.startswith(b"(\xb5/\xfd"):  # zstd 0xFD2FB528 LE
            # https://github.com/facebook/zstd/blob/dev/doc/zstd_compression_format.md#zstandard-frames
            reader = _open_zstd(buffered_stream, mode)
        elif magic.startswith(b'\x04"M\x18'):  # lz4 0x184D2204 LE
            # https://github.com/lz4/lz4/blob/dev/doc/lz4_Frame_format.md#general-structure-of-lz4-frame-format
            reader = _open_lz4(buffered_stream, mode)
        elif magic.startswith(b"\xfd7zXZ\x00"):  # lzma/xz FD 37 7A 58 5A 00
            # https://github.com/tukaani-project/xz/blob/master/doc/xz-file-format.txt
            reader = lzma.open(
                buffered_stream,
                mode=mode,
                encoding=encoding,
                errors=errors,
            )
        elif _is_valid_bzip2(buffered_stream):  # bzip2
            reader = bz2.open(
                buffered_stream,
                mode=mode,
                encoding=encoding,
                errors=errors,
            )
        else:
            # Fallback for plain text files
            if mode == "rt":
                reader = io.TextIOWrapper(buffered_stream, encoding=encoding, errors=errors)
            else:
                reader = buffered_stream
        yield reader
    finally:
        if reader is not None:
            reader.close()
        if buffered_stream is not None:
            buffered_stream.close()
        if raw_stream is not None:
            raw_stream.close()


def _is_valid_bzip2(buffered_stream):
    """
    Validate whether the file is a valid bzip2 file by inspecting the header
    and analyzing additional bytes to differentiate plain text from binary data.
    """
    # Peek enough bytes for header validation and initial data analysis
    magic_bytes = buffered_stream.peek(64)

    # Check the magic header: BZh[1-9] (https://en.wikipedia.org/wiki/Bzip2#File_format)
    # The magic header is all ASCII, so to prevent reading plain text as bz2, check for binary data after.
    # magic[0:3] == b"BZh" and magic[5:10] == b"1AY&SY"
    # 425a 68xx 3141 5926 5359

    if not (magic_bytes.startswith(b"BZh")
            and b"1" <= magic_bytes[3:4] <= b"9"
            and magic_bytes[5:10] == b"1AY&SY"):
        return False

    # Read beyond the header for further inspection
    additional_data = magic_bytes[10:]  # Bytes after "BZh[1-9]" and pi

    # Check if the data following the header conforms to compressed binary data characteristics
    if _looks_like_binary_data(additional_data):
        # Optionally, test-decompress a small chunk for verification
        try:
            decompressor = bz2.BZ2Decompressor()
            decompressor.decompress(magic_bytes)  # Testing small decompression
            return True  # Valid bzip2 file
        except OSError:
            return False  # Failed decompression
    return False


def _looks_like_binary_data(data):
    # Check if most of the data is non-printable characters
    # Plain ASCII (text): bytes 32-126, plus whitespace (tab, newline, etc.)
    binary_threshold = 0.1  # At least 10% non-printable data
    non_printable = sum(1 for byte in data if byte < 32 or byte > 126)
    return (non_printable / len(data)) > binary_threshold if data else False


def _open_zstd(buffered_stream, mode):
    """Open a Zstandard-compressed file for reading."""
    dctx = zstd.ZstdDecompressor()
    reader = dctx.stream_reader(buffered_stream)
    if mode == "rt":
        return io.TextIOWrapper(reader, encoding="utf-8", errors="ignore")
    return reader


def _open_lz4(buffered_stream, mode):
    """Open an LZ4-compressed file for reading."""
    reader = LZ4FrameFile(buffered_stream)
    if mode == "rt":
        return io.TextIOWrapper(reader, encoding="utf-8", errors="ignore")
    return reader


def read_records(listing):
    listing_stat = os.stat(listing)
    logger.info(f"Opening listing {listing}")

    with open_maybe_compressed(listing, "rt") as f:
        for line in f:
            line = line.removesuffix("\n").removesuffix("\0")
            record_json = None
            if line.startswith("{") or line.startswith("["):
                try:
                    record_json = json.loads(line)
                except json.JSONDecodeError:
                    pass

            if isinstance(record_json, list):
                if len(record_json) == 3:
                    mtime_ns = int(float(record_json[0]) * 1e9)
                    path = record_json[2]
                    typ = "d" if path.endswith("/") else "f"
                    mode = (0o755 if path.endswith("/") else 0o644) | filetype_to_mode[typ]
                    size = record_json[1]
                    record = Record(
                        mtime_ns=mtime_ns,
                        bytes=size,
                        block_kib=math.ceil(size / 1024),
                        path=path,
                        typ=typ,
                        mode=mode,
                    )
                    yield record
                    continue
                if len(record_json) == 4:
                    mtime_ns = int(float(record_json[0]) * 1e9)
                    path = record_json[3]
                    typ = "d" if path.endswith("/") else "f"
                    mode = (0o755 if path.endswith("/") else 0o644) | filetype_to_mode[typ]
                    record = Record(
                        mtime_ns=mtime_ns,
                        bytes=record_json[1],
                        block_kib=record_json[2],
                        path=path,
                        typ=typ,
                        mode=mode,
                    )
                    yield record
                    continue
            elif isinstance(record_json, dict):
                mtime_ns = int(float(record_json["t"]) * 1e9)
                typ = record_json["y"] if "y" in record_json else "d" if record_json["p"].endswith("/") else "f"
                mode = int(record_json["m"], 8) | filetype_to_mode[typ]
                size = record_json.get("s", 0)
                record = Record(
                    mtime_ns=mtime_ns,
                    bytes=size,
                    path=record_json["p"],
                    typ=typ,
                    mode=mode,
                    src_inode=int(record_json["i"]) if "i" in record_json else None,
                    block_kib=record_json.get("k", math.ceil(size / 1024)),
                    target=record_json.get("l"),
                    empty=record_json.get("e", False),
                )
                yield record
                continue

            gnu_tar_matched = gnu_tar_format_re.match(line)
            if gnu_tar_matched:
                target = None
                typ, perms, has_xattrs, user, group, size, major, minor, mtime, path = gnu_tar_matched.groups()
                path = unquote_gnulib(path)
                if typ == "l":
                    path, target = path.split(" -> ", 1)
                if typ == "h":
                    # NOTE: we're treating hard links like files, could be more robust
                    # TODO: " link to " is locale-dependent. This is hardcoded for English.
                    #       the big regex could split on it, but splitting here makes locale support later easier.
                    path, target = path.split(" link to ", 1)

                colon_count = mtime.count(":")
                if colon_count == 1:
                    mtime_ns = int(datetime.strptime(mtime, "%Y-%m-%d %H:%M").timestamp() * 1e9)
                elif mtime.count(".") == 1:
                    truncated_mtime = mtime[:26]  # ValueError('unconverted data remains: 001') for smaller fractions of a second
                    mtime_ns = int(datetime.strptime(truncated_mtime, "%Y-%m-%d %H:%M:%S.%f").timestamp() * 1e9)
                elif colon_count == 2:
                    mtime_ns = int(datetime.strptime(mtime, "%Y-%m-%d %H:%M:%S").timestamp() * 1e9)
                else:
                    raise ValueError(f"unexpected mtime format: {mtime}, {listing}, {path}")
                size = int(size) if size else 0
                record = Record(
                    mtime_ns=mtime_ns,
                    typ=typ,
                    bytes=size,
                    path=path,
                    mode=fileperm_to_mode(perms) | filetype_to_mode[typ],
                    block_kib=math.ceil(size / 1024),
                    target=target,
                    src_user=sys.intern(user),
                    src_group=sys.intern(group),
                )
                yield record
                continue

            find_ls_matched = find_ls_format_re.match(line)
            if find_ls_matched:
                src_inode, block_kib, typ, perms, link_no, user, group, size, major, minor, date, path = find_ls_matched.groups()
                fallback_year = datetime.fromtimestamp(listing_stat.st_mtime).year
                mtime_ns = int(parse_ls_date(date, fallback_year).timestamp() * 1e9)
                path = unquote_gnulib(path)
                record = Record(
                    src_inode=int(src_inode),
                    block_kib=int(block_kib),
                    typ=typ,
                    mode=fileperm_to_mode(perms) | filetype_to_mode[typ],
                    src_user=sys.intern(user),
                    src_group=sys.intern(group),
                    bytes=int(size),
                    mtime_ns=mtime_ns,
                    path=path,
                )
                yield record
                continue

            tabular_matched = tabular_format_re.match(line)
            if tabular_matched:
                ts, size, path = tabular_matched.groups()
                mtime_ns = int(float(ts) * 1e9)
                typ = "d" if path.endswith("/") else "f"
                mode = (0o755 if typ == "/" else 0o644) | filetype_to_mode[typ]
                size = int(size)
                block_kib = math.ceil(size / 1024)
                record = Record(
                    mtime_ns=mtime_ns,
                    typ=typ,
                    mode=mode,
                    bytes=size,
                    block_kib=block_kib,
                    path=path,
                )
                yield record
                continue

            if line.startswith("#") or line.startswith("//"):
                # Expected line to ignore
                continue
            # if re.match(r"^File number=[-\d]+, block number=[-\d]+, partition=[-\d]+.$", line):
            if line.startswith("File number="):
                # Expected line to ignore
                continue

            # assume the line is a literal path string now
            typ = "d" if line.endswith("/") else "f"
            mode = (0o755 if typ == "d" else 0o644) | filetype_to_mode[typ]
            record = Record(
                mtime_ns=int(listing_stat.st_mtime * 1e9),
                bytes=0,
                path=line,
                typ=typ,
                mode=mode,
            )
            yield record


class Record:  # Basically the same as Meta but with path and no src_listing
    """A loaded line from a listing, before being processed into a node"""
    __slots__ = (
        "mode",
        "mtime_ns",
        "path",
        "bytes",
        "src_inode",
        "block_kib",
        "target",
        "src_user",
        "src_group",
        "typ",
        "empty",
    )

    def __init__(
            self,
            mode: int,
            mtime_ns: int,
            path: str,
            bytes: int = 0,
            src_inode: int | None = None,
            block_kib: int = 0,
            target: str | None = None,
            src_user: str | None = None,
            src_group: str | None = None,
            typ: str | None = None,
            empty: bool = False,
    ):
        self.mode = mode
        self.mtime_ns = mtime_ns
        self.path = path
        self.bytes = bytes
        self.src_inode = src_inode
        self.block_kib = block_kib
        self.target = target
        self.src_user = src_user
        self.src_group = src_group
        self.typ = typ
        self.empty = empty


class Meta:
    __slots__ = (
        "src_listing",
        "mode",
        "mtime_ns",
        "bytes",
        "src_inode",
        "block_kib",
        "target",
        "src_user",
        "src_group",
    )

    def __init__(
            self,
            src_listing: str,
            mode: int,
            mtime_ns: int,
            bytes: int = 0,
            src_inode: int | None = None,
            block_kib: int = 0,
            target: str | None = None,
            src_user: str | None = None,
            src_group: str | None = None,
    ):
        self.src_listing = src_listing
        self.mode = mode
        self.mtime_ns = mtime_ns
        self.bytes = bytes
        self.src_inode = src_inode
        self.block_kib = block_kib
        self.target = target
        self.src_user = src_user
        self.src_group = src_group

    def __iter__(self):
        for key in self.__slots__:
            yield key, getattr(self, key)


class Node:
    __slots__ = (
        "name",
        "st_ino",
        "meta_dirs",
        "meta_other",
        "meta_implicit",
        "meta_implicit_listings",
        "children",
        # "__weakref__",
    )

    def __init__(
            self,
            name: str,
            st_ino: pyfuse3.InodeT,
            meta_dirs: List[Meta] | Tuple[Meta, ...] | None = None,
            meta_other: List[Meta] | Tuple[Meta, ...] | None = None,
            meta_implicit: List[Meta] | Tuple[Meta, ...] | None = None,
            meta_implicit_listings: set[str] | frozenset[str] | None = None,
            children: Dict[str, pyfuse3.InodeT] | None = None,
    ):
        self.name = name
        self.st_ino = st_ino
        self.meta_dirs = meta_dirs
        self.meta_other = meta_other
        self.meta_implicit = meta_implicit
        self.meta_implicit_listings = meta_implicit_listings if meta_implicit_listings is not None else set()
        self.children = children

    def get_meta(self) -> Meta:
        if self.meta_dirs:  # Explicit directories first
            return self.meta_dirs[0]
        if self.meta_implicit:  # Implicit directories next
            return self.meta_implicit[0]
        if self.meta_other:  # Other file types last
            return self.meta_other[0]
        raise ValueError("Node should be created with at least one Meta")

    def get_metas(self) -> Sequence[Meta]:
        metas = []
        if self.meta_dirs is not None:
            metas.extend(self.meta_dirs)
        if self.meta_other is not None:
            metas.extend(self.meta_other)
        if self.meta_implicit is not None:
            metas.extend(self.meta_implicit)
        return metas


@dataclass
class ListFsOptions:
    uid: int = os.getuid()
    gid: int = os.getgid()


class ListFS(pyfuse3.Operations):
    def __init__(self, listfs_options: ListFsOptions):
        super().__init__()
        self.options = listfs_options

        self.node_root = Node(
            name="",
            st_ino=pyfuse3.ROOT_INODE,
            meta_implicit=([
                Meta(
                    src_listing="",
                    mode=stat.S_IFDIR | 0o755,
                    mtime_ns=0,
                )
            ]),
        )
        # IDE complained about type when assigning children in the Node constructor
        # self.node_root.children = WeakValueDictionary()
        self.node_root.children = {}

        # self.nodes: WeakValueDictionary[InodeT, Node] = WeakValueDictionary()
        self.nodes: dict[InodeT, Node] = {}
        self.nodes[pyfuse3.ROOT_INODE] = self.node_root

        self.parent: Dict[InodeT, InodeT] = {pyfuse3.ROOT_INODE: pyfuse3.ROOT_INODE}

        # self.node_lookup: WeakValueDictionary[str, Node] = WeakValueDictionary()

        self._next_inode = pyfuse3.ROOT_INODE + 1
        # self.dir_insert_cache: OrderedDict[str, ref[Node]] | None = OrderedDict()
        self.dir_insert_cache: OrderedDict[Tuple[str, ...], Node] | None = OrderedDict()
        self.loads = 0
        self.perf_start = perf_counter()
        self.loads_since_last_log = 0
        self.perf_last_log = 0

        self._list_size = 0
        self._tuple_size = 0

        self._total_bytes = 0
        self._total_blocks = 0

    def _allocate_node(self, name, parent_node):
        inode = InodeT(self._next_inode)
        self._next_inode += 1
        node = Node(name, st_ino=inode)
        self.nodes[inode] = node
        parent_node.children[name] = inode
        self.parent[inode] = parent_node.st_ino
        return node

    def _lookup_in_cache(self, path_parts: Tuple) -> Tuple[Node, int]:
        """
        Check the LRU cache for the nearest ancestor directory node.
        Return the node and depth if matched, else None and start from the root.
        """
        if not self.dir_insert_cache:
            return self.node_root, 0
        for i in range(len(path_parts), 0, -1):
            sub_path = path_parts[:i]
            if sub_path in self.dir_insert_cache:
                # node_ref: ref[Node] = self.dir_insert_cache[sub_path]
                # node = node_ref()
                # if node is not None:
                #     return node, i

                node = self.dir_insert_cache[sub_path]
                if node is not None:
                    return node, i
        return self.node_root, 0  # Start from the root if no match exists

    def _update_cache(self, path_part_slice: Tuple[str, ...], node: Node):
        """
        Update the LRU cache with the given path and node.
        Evicts the least recently used entry if the cache exceeds its limit.
        """
        if path_part_slice in self.dir_insert_cache:
            # Move the entry to the end (most recently used)
            self.dir_insert_cache.move_to_end(path_part_slice)
        else:
            # self.dir_insert_cache[path] = ref(node)
            self.dir_insert_cache[path_part_slice] = node
            if len(self.dir_insert_cache) > 20:  # Cache limit
                self.dir_insert_cache.popitem(last=False)  # Evict least recently used

    def calculate_size(self):
        logger.info("Calculating total size...")
        bytes_ = 0
        blocks = 0
        for node in self.nodes.values():
            meta = node.get_meta()
            blocks += meta.block_kib
            bytes_ += meta.bytes
        self._total_blocks = blocks
        self._total_bytes = bytes_

    def load_listing(self, file, skip_components=0, prefix_dir=None):
        skip_root_state = {}
        if prefix_dir:
            prefix_parts = tuple(part for part in prefix_dir.split("/") if part not in (".", ""))
        else:
            prefix_parts = tuple()

        # TODO: store the last 20 directory nodes and their paths to a LRU cache,
        #  so that if the next node being inserted shares a parent directory,
        #  it doesn't need to walk the whole tree again.

        def insert_node(record):
            if self.loads % 10000 == 0:
                perf_now = perf_counter()
                if perf_now - self.perf_last_log > 5:
                    logger.info(f"Percent complete: {(100 * self.loads / total_line_count):.2f}%; "
                                f"Total loaded records so far: {self.loads}; "
                                f"Records per second: {self.loads_since_last_log / (perf_now - self.perf_last_log):.0f}"
                                )
                    self.perf_last_log = perf_now
                    self.loads_since_last_log = 0
            self.loads += 1
            self.loads_since_last_log += 1
            path_parts = tuple(part for part in record.path.split("/") if part not in (".", ""))
            if skip_components:
                if len(path_parts) < skip_components:
                    return
                root_dir = path_parts[:skip_components]
                if "root_dir" not in skip_root_state:
                    skip_root_state["root_dir"] = root_dir
                if skip_root_state["root_dir"] != root_dir:
                    raise KeyError(f"Unable to skip {skip_components} components on listing {file}; conflicting paths: {json.dumps(skip_root_state["root_dir"])}, {json.dumps(root_dir)}")

            mounted_path_parts = tuple(prefix_parts + path_parts[skip_components:])

            # parent_node = self.nodes[pyfuse3.ROOT_INODE]
            parent_node, start_at = self._lookup_in_cache(mounted_path_parts[:-1])

            # Check for closest lookup node. We store lookups in 2 part increments.
            # Example:
            # path is "/docs/foo/bar/baz/quux/aaa/bbb"
            # mounted_path_parts is ["docs", "foo", "bar", "baz", "quux", "aaa", "bbb"]
            # mounted_path_parts is 7 items long, so go to the longest multiple of 2 first, which is 6 in this case:
            # lookup_check = "/".join(mounted_path_parts[:6])
            # if lookup_check in self.node_lookup:
            #     # "/docs/foo/bar/baz/quux/aaa" has a node
            #     start_at=6

            # Commenting... I thought this would be faster, but it might use a lot more memory.
            # start_at = ((len(mounted_path_parts) - 1) // 2) * 2
            # # Iterate through substrings of full_mounted_path to find the first match in self.node_lookup
            # while start_at > 0:
            #     substring = "/".join(mounted_path_parts[:start_at])
            #     if substring in self.node_lookup:
            #         parent_node = self.node_lookup[substring]
            #         break
            #     start_at -= 2

            for i, part in enumerate(mounted_path_parts[start_at:], start_at):
                # get node
                part = sys.intern(part)
                if parent_node.children is None:  # Can be none if detected type was file, but later a child is added
                    # parent_node.children = WeakValueDictionary()
                    parent_node.children = {}
                    node = self._allocate_node(part, parent_node)
                elif part in parent_node.children:
                    node = self.nodes[parent_node.children[part]]
                else:
                    node = self._allocate_node(part, parent_node)

                self._update_cache(mounted_path_parts[:i + 1], node)
                last_part = i == len(mounted_path_parts) - 1
                if last_part:
                    # Fill in leaf
                    # TODO handle hard links
                    meta = Meta(
                        src_listing=file,
                        mode=record.mode,
                        mtime_ns=record.mtime_ns,
                        bytes=record.bytes,
                        src_inode=record.src_inode,
                        block_kib=record.block_kib,
                        target=os.fsencode(record.target) if record.target is not None else None,
                        src_user=record.src_user,
                        src_group=record.src_group,
                    )
                    if stat.S_ISDIR(record.mode):
                        # if (i + 1) % 2 == 0:
                        #     self.node_lookup["/".join(mounted_path_parts[: i + 1])] = node
                        if node.meta_dirs is None:
                            node.meta_dirs = [meta]
                        else:
                            node.meta_dirs.append(meta)
                            # node.meta_dirs.sort(key=lambda x: x.mtime_ns, reverse=True)
                        if node.children is None:
                            # node.children = WeakValueDictionary()
                            node.children = {}
                    else:
                        if node.meta_other is None:
                            node.meta_other = [meta]
                        else:
                            node.meta_other.append(meta)
                            # node.meta_other.sort(key=lambda x: x.mtime_ns, reverse=True)
                else:
                    # Fill in branch
                    # if (i + 1) % 2 == 0:
                    #     self.node_lookup["/".join(mounted_path_parts[: i + 1])] = node
                    if file not in node.meta_implicit_listings:
                        node.meta_implicit_listings.add(file)
                        meta = Meta(
                            src_listing=file,
                            mode=stat.S_IFDIR | 0o755,
                            mtime_ns=record.mtime_ns,
                        )
                        if node.meta_implicit is None:
                            node.meta_implicit = [meta]
                        else:
                            node.meta_implicit.append(meta)
                            # node.meta_implicit.sort(key=lambda x: x.mtime_ns, reverse=True)
                    if not node.children:
                        # node.children = WeakValueDictionary()
                        node.children = {}
                    parent_node = node

        for record in read_records(file):
            insert_node(record)

        listing_stat = os.stat(file)
        if file not in self.node_root.meta_implicit_listings:
            self.node_root.meta_implicit_listings.add(file)
            self.node_root.meta_implicit.append(Meta(
                src_listing=file,
                mode=stat.S_IFDIR | 0o755,
                mtime_ns=listing_stat.st_mtime_ns,
            ))
            # self.node_root.meta_implicit.sort(key=lambda x: x.mtime_ns, reverse=True)
        logger.info(
            f"Total percent complete: {(100 * self.loads / total_line_count):.2f}%; "
            f"Total loaded records so far: {self.loads}; "
            f"Records per second: {self.loads / (perf_counter() - self.perf_start):.0f}; "
            f"Finished loading {file}"
        )

    async def lookup(
        self,
        parent_inode: InodeT,
        name: FileNameT,
        ctx: pyfuse3.RequestContext = None
    ) -> pyfuse3.EntryAttributes:
        if name == b".":
            inode = parent_inode
        elif name == b"..":
            inode = self.parent[parent_inode]
        else:
            children = self.nodes[parent_inode].children
            if children is None:
                raise pyfuse3.FUSEError(errno.ENOENT)
            inode = children.get(os.fsdecode(name))
            if inode is None:
                raise pyfuse3.FUSEError(errno.ENOENT)
            node = self.nodes[inode]
            if not node:
                raise pyfuse3.FUSEError(errno.ENOENT)
            inode = node.st_ino
        return await self.getattr(inode, ctx)

    async def getattr(
        self, inode: InodeT, ctx: pyfuse3.RequestContext = None
    ) -> pyfuse3.EntryAttributes:
        node = self.nodes.get(inode)
        if node is None:
            raise pyfuse3.FUSEError(errno.ENOENT)
        if node.meta_dirs:  # Explicit directories first
            meta = node.meta_dirs[0]
        elif node.meta_implicit:  # Implicit directories next
            meta = node.meta_implicit[0]
        elif node.meta_other:  # Other file types last
            meta = node.meta_other[0]
        else:
            raise pyfuse3.FUSEError(errno.ENOENT)

        entry = pyfuse3.EntryAttributes()
        entry.st_ino = inode
        entry.generation = 0
        # entry.entry_timeout
        # entry.attr_timeout
        entry.st_mode = pyfuse3.ModeT(meta.mode)
        # TODO handle hardlinks on files

        if not stat.S_ISDIR(meta.mode):
            st_nlink = 1
        else:
            st_nlink = 2  # 1 for "." and 1 for ".."
            # Nice to have, and correct, but maybe slow:
            # if node.children is not None:
            #     for child_name, child_inode in node.children.items():
            #         child = self.nodes.get(child_inode)
            #         if child is not None:
            #             if child.meta_dirs is not None and len(child.meta_dirs) > 0:
            #                 st_nlink += 1
            #             elif child.meta_implicit is not None and len(child.meta_implicit) > 0:
            #                 st_nlink += 1
        entry.st_nlink = st_nlink

        entry.st_uid = self.options.uid
        entry.st_gid = self.options.gid
        # entry.st_rdev
        entry.st_size = meta.bytes
        # entry.st_size = 0
        # entry.st_blksize = 512
        # entry.st_blocks = meta.block_kib * 2
        entry.st_blksize = 1024
        entry.st_blocks = meta.block_kib
        # entry.st_blocks = 0
        entry.st_mtime_ns = meta.mtime_ns
        entry.st_atime_ns = entry.st_mtime_ns
        entry.st_ctime_ns = entry.st_mtime_ns
        return entry

    async def readlink(
        self, inode: InodeT, ctx: pyfuse3.RequestContext = None
    ) -> FileNameT:
        if inode not in self.nodes:
            raise pyfuse3.FUSEError(errno.ENOENT)
        node = self.nodes[inode]
        if node.meta_other is None or len(node.meta_other) == 0:
            raise pyfuse3.FUSEError(errno.EINVAL)
        meta = node.meta_other[0]
        if meta.target is None:
            raise pyfuse3.FUSEError(errno.EINVAL)
        return FileNameT(os.fsencode(meta.target))

    async def open(
        self,
        inode: pyfuse3.InodeT,
        flags: pyfuse3.FlagT,
        ctx: pyfuse3.RequestContext = None,
    ):
        attr = await self.getattr(inode)
        file_info = pyfuse3.FileInfo(
            fh=pyfuse3.FileHandleT(attr.st_ino),
            direct_io=True,
            keep_cache=False,
            nonseekable=True,
        )
        return file_info

    async def read(self, fh: FileHandleT, offset: int, length: int) -> bytes:
        node = self.nodes[InodeT(fh)]
        metas = node.get_metas()
        attrs = []
        for meta in metas:
            meta_dict = dict(meta)
            meta_dict["mode"] = stat.filemode(meta.mode)
            meta_dict["mtime_ns"] = datetime.fromtimestamp(meta.mtime_ns / 1e9).isoformat()
            attrs.append(meta_dict)
        # Add #!/bin/false so that any executable files don't accidentally do something bad
        return ("#!/bin/false\n" + json.dumps(attrs, indent=4) + "\n").encode()[offset:offset + length]

    async def flush(self, fh: FileHandleT) -> None:
        pass

    async def release(self, fh: FileHandleT) -> None:
        pass

    async def opendir(
        self, inode: InodeT, ctx: pyfuse3.RequestContext = None
    ) -> FileHandleT:
        return FileHandleT(inode)

    async def readdir(
        self, inode: pyfuse3.FileHandleT, start_id: int, token: pyfuse3.ReaddirToken
    ) -> None:
        inode_ = InodeT(inode)
        if inode_ not in self.nodes:
            raise pyfuse3.FUSEError(errno.ENOENT)
        if start_id == 0:
            attrs = await self.getattr(inode_)
            reply_ok = pyfuse3.readdir_reply(token, FileNameT(b"."), attrs, start_id + 1)
            if not reply_ok:
                return
            start_id += 1
        if start_id == 1:
            attrs = await self.getattr(self.parent[inode_])
            reply_ok = pyfuse3.readdir_reply(token, FileNameT(b".."), attrs, start_id + 1)
            if not reply_ok:
                return
            start_id += 1
        node = self.nodes[inode_]
        for name, child_inode in islice(node.children.items(), start_id - 2, None):
            attrs = await self.getattr(child_inode)
            reply_ok = pyfuse3.readdir_reply(token, FileNameT(os.fsencode(name)), attrs, start_id + 1)
            if not reply_ok:
                return
            start_id += 1

    async def releasedir(self, fh: FileHandleT) -> None:
        pass

    async def statfs(self, ctx: pyfuse3.RequestContext = None) -> pyfuse3.StatvfsData:
        # man statvfs
        stat_ = pyfuse3.StatvfsData()
        stat_.f_bsize = 1024
        stat_.f_frsize = 1024  # 1 would work fine too
        # f_blocks is in frsize units.
        # Use total_bytes because records are more likely to have byte size than block size
        stat_.f_blocks = math.ceil(self._total_bytes / 1024)  # Could use int directly if frsize is 1
        stat_.f_bfree = 0
        stat_.f_bavail = 0
        stat_.f_files = len(self.nodes)
        stat_.f_ffree = 0
        stat_.f_favail = 0
        stat_.f_namemax = 255  # Could be lengthened?
        return stat_

    async def getxattr(
        self,
        inode: pyfuse3.InodeT,
        name: pyfuse3.XAttrNameT,
        ctx: pyfuse3.RequestContext = None,
    ) -> bytes:
        name_str = os.fsdecode(name)
        if not name_str.startswith("user."):
            raise pyfuse3.FUSEError(errno.ENODATA)
        name_u = name_str.removeprefix("user.")
        # Use :: to separate listing filename from column name
        src_listing, _, xattr_name = name_u.partition("::")
        src_listing, _, index = src_listing.rpartition("_")
        if not xattr_name or not index:
            raise pyfuse3.FUSEError(errno.ENODATA)
        try:
            index = int(index)
        except ValueError:
            raise pyfuse3.FUSEError(errno.ENODATA)
        node = self.nodes[inode]
        metas = node.get_metas()
        if not metas:
            raise pyfuse3.FUSEError(errno.ENODATA)
        grouped_src_metas = defaultdict(list)
        for meta in metas:
            grouped_src_metas[meta.src_listing].append(meta)
        try:
            meta = grouped_src_metas[src_listing][index]
            if xattr_name == "mtime_str":  # Calculated for convenience
                value = datetime.fromtimestamp(meta.mtime_ns / 1e9).isoformat()
            elif xattr_name == "fileperm":  # Calculated for convenience
                value = stat.filemode(meta.mode)
            else:
                value = dict(meta).get(xattr_name)
            if not isinstance(value, str):
                value = json.dumps(value)
            return os.fsencode(value)
        except IndexError:
            raise pyfuse3.FUSEError(errno.ENODATA)

    async def listxattr(
        self, inode: pyfuse3.InodeT, ctx: pyfuse3.RequestContext = None
    ) -> Sequence[pyfuse3.XAttrNameT]:
        node: Node = self.nodes[inode]
        metas = node.get_metas()
        grouped_src_metas = defaultdict(list)
        for meta in metas:
            grouped_src_metas[meta.src_listing].append(meta)
        xattrs = []
        for src_listing, metas in grouped_src_metas.items():
            for n in range(len(metas)):
                for k, v in dict(metas[n]).items():
                    xattrs.append(pyfuse3.XAttrNameT(os.fsencode(f"user.{src_listing}_{n}::{k}")))
                xattrs.append(os.fsencode(f"user.{src_listing}_{n}::mtime_str"))  # Calculated value for convenience
                xattrs.append(os.fsencode(f"user.{src_listing}_{n}::fileperm"))  # Calculated value for convenience
        xattrs.sort()
        return xattrs

    def pack_memory(self):
        self.dir_insert_cache = None

        logger.info("Packing lists...")
        # Remove any preallocated memory for lists
        for node in self.nodes.values():
            self._list_size += sys.getsizeof(node.meta_dirs)
            self._list_size += sys.getsizeof(node.meta_other)
            self._list_size += sys.getsizeof(node.meta_implicit)

        for node in self.nodes.values():
            if node.meta_dirs is not None:
                node.meta_dirs = tuple(node.meta_dirs)
            if node.meta_other is not None:
                node.meta_other = tuple(node.meta_other)
            if node.meta_implicit is not None:
                node.meta_implicit = tuple(node.meta_implicit)
            del node.meta_implicit_listings

        for node in self.nodes.values():
            self._tuple_size += sys.getsizeof(node.meta_dirs)
            self._tuple_size += sys.getsizeof(node.meta_other)
            self._tuple_size += sys.getsizeof(node.meta_implicit)

        logger.info("Lists packed.")
        logger.info(f"Size before : {self._list_size}")
        logger.info(f"Size after  : {self._tuple_size}")


def parse_args(args: list[str]):
    # It was easier to manually parse than to use argparse or click.
    # Docopt might have worked, but is not maintained.
    options = []
    foreground = False
    listings = []
    mountpoint = None
    skip_components = -1
    prefix_dir = None
    expect_options = False
    expect_skip = False
    expect_prefix = False
    listing_options_started = False

    for i, arg in enumerate(args):
        if arg in ["--help", "-h"]:
            print(__doc__)
            sys.exit(0)
        if arg == "--help-formats":
            print(format_help)
            sys.exit(0)
        if arg == "--version":
            print(textwrap.dedent(f"""
            listfs-py version {__version__}
            Copyright listfs authors. Distributed under GPL-3.0-or-later
            """).strip())
            sys.exit(0)
        if (expect_options or arg.startswith("--options=")) and listing_options_started:
            raise ValueError("--options must be specified before listing-related options")
        if expect_options:
            options.extend(arg.split(","))
            expect_options = False
        elif arg == "--options" or arg == "-o":
            expect_options = True
        elif arg.startswith("--options="):
            options.extend(arg.partition("=")[2].split(","))
        elif arg == "--foreground":
            if listing_options_started:
                raise ValueError("--foreground must be specified before listing-related options")
            foreground = True
        elif expect_skip:
            skip_components = int(arg)
            if skip_components < 0:
                raise ValueError("Cannot specify --skip-components less than 0")
            expect_skip = False
        elif arg == "--skip-components":
            if skip_components > -1:
                raise ValueError("Cannot specify --skip-components twice on the same listing")
            expect_skip = True
        elif arg.startswith("--skip-components="):
            if skip_components > -1:
                raise ValueError("Cannot specify --skip-components twice on the same listing")
            skip_components = int(arg.partition("=")[2])
        elif expect_prefix:
            prefix_dir = arg
            expect_prefix = False
        elif arg == "--prefix-dir":
            if prefix_dir is not None:
                raise ValueError("Cannot specify --prefix-dir twice on the same listing")
            expect_prefix = True
        elif arg.startswith("--prefix-dir="):
            if prefix_dir is not None:
                raise ValueError("Cannot specify --prefix-dir twice on the same listing")
            prefix_dir = arg.partition("=")[2]
        elif i == len(args) - 1:
            if expect_skip or expect_prefix:
                raise ValueError("Missing argument for --skip-components or --prefix-dir")
            if not os.path.isdir(arg):
                raise ValueError(f"Mountpoint is not a directory: {arg}")
            mountpoint = arg
        else:
            if skip_components < 0:
                skip_components = 0
            # Check if arg is a regular file and exists:
            if not os.path.isfile(arg):
                raise ValueError(f"Listing is not a file: {arg}")
            listings.append({
                "file": arg,
                "skip_components": skip_components,
                "prefix_dir": prefix_dir,
            })
            listing_options_started = True
            skip_components = -1
            prefix_dir = None
    if mountpoint is None:
        raise ValueError("Missing mountpoint")
    if not listings:
        raise ValueError("Missing listings")

    return [options, foreground, mountpoint, listings]


def transform_user_options(options):
    options = set(options)
    fs_options = ListFsOptions()
    if "rw" in options:
        logger.warning("listfs does not support the rw option; ignoring it")
        options.remove("rw")
    for option in options.copy():
        if option.startswith("fsname="):
            logger.debug("discarding custom fsname option")
            options.remove(option)
        if option.startswith("uid="):
            uid = option.removeprefix("uid=")
            try:
                fs_options.uid = pwd.getpwuid(int(uid)).pw_uid
            except Exception as e:
                try:
                    fs_options.uid = pwd.getpwnam(uid).pw_uid
                except Exception as e:
                    logger.error("Not able to read uid", exc_info=e)
                    sys.exit(1)
            options.remove(option)
        if option.startswith("gid="):
            gid = option.removeprefix("gid=")
            try:
                fs_options.gid = grp.getgrgid(int(gid)).gr_gid
            except Exception as e:
                try:
                    fs_options.gid = grp.getgrnam(gid).gr_gid
                except Exception as e:
                    logger.error("Not able to read gid", exc_info=e)
                    sys.exit(1)
            options.remove(option)
    if fs_options.uid != os.getuid() and "allow_other" not in options:
        logger.warning("uid option specified for another user, but the other user will not be able to read unless allow_other is also specified")
    return fs_options, options


def get_fuse_options(options):
    fuse_options = set(pyfuse3.default_options)
    fuse_options.update(options)
    fuse_options.add("fsname=listfs")
    # fuse_options.add("allow_other")
    fuse_options.add("ro")

    # Prints "fusermount3: /mnt not mounted" if not auto unmounted by fuse
    # fuse_options.add("auto_unmount")

    # fuse_options.add("debug")
    return fuse_options


def load_all_listings(listings, operations):
    global total_line_count
    for listing in listings:
        # line_count = buf_count_newlines_gen(listing["file"])
        line_count = count_lines(listing["file"])
        logger.info(f"Listing {listing["file"]} has {line_count} lines")
        total_line_count += line_count
    logger.info(f"Total listing lines: {total_line_count}")
    if total_line_count == 0:
        logger.error("Cowardly refusing to mount an empty filesystem")
        sys.exit(1)
    logger.info("Loading listings...")

    for listing in listings:
        operations.load_listing(
            listing["file"],
            listing["skip_components"],
            listing["prefix_dir"],
        )

    logger.info(
        f"Percent complete: 100%; "
        f"Total lines: {total_line_count}; "
        f"Total records: {operations.loads}; "
        f"Records per second: {operations.loads / (perf_counter() - operations.perf_start):.0f}"
    )

    logger.info("Preparing timestamps...")
    for node in operations.nodes.values():
        if node.meta_dirs is not None:
            node.meta_dirs.sort(key=lambda x: x.mtime_ns, reverse=True)
        if node.meta_implicit is not None:
            node.meta_implicit.sort(key=lambda x: x.mtime_ns, reverse=True)
        if node.meta_other is not None:
            node.meta_other.sort(key=lambda x: x.mtime_ns, reverse=True)

    operations.calculate_size()


def count_lines(filename):
    try:
        with open_maybe_compressed(filename, mode="rt") as f:
            return sum(1 for _ in f)
    except Exception as e:
        logger.error(f"Error counting lines in listing {filename}: {e}")
        return 0


def daemonize():
    logger.info("Daemonizing...")
    gc.freeze()
    try:
        if os.fork() > 0:  # Exit parent process, child to be daemonized
            sys.exit()
    except OSError as e:
        logger.error(f"fork #1 failed: {e}")
        sys.exit(1)
    os.setsid()  # Create a new session
    try:
        if os.fork():  # Fork again to ensure the process cannot acquire a terminal
            sys.exit()
    except OSError as e:
        logger.error(f"fork #2 failed: {e}")
        sys.exit(1)
    os.chdir("/")  # Prevent locks on filesystem we started in; allow unmounts
    os.umask(0)
    sys.stdout.flush()
    sys.stderr.flush()
    with open("/dev/null", "rb") as devnull:
        os.dup2(devnull.fileno(), sys.stdin.fileno())
    with open("/dev/null", "wb") as devnull:
        os.dup2(devnull.fileno(), sys.stdout.fileno())
        os.dup2(devnull.fileno(), sys.stderr.fileno())
    gc.unfreeze()


async def signal_handler(cancel_scope):
    with trio.open_signal_receiver(signal.SIGINT, signal.SIGQUIT, signal.SIGTERM) as signal_aiter:
        async for sig in signal_aiter:
            logger.info(f"Received signal {signal.Signals(sig).name}; exiting")
            cancel_scope.cancel()
            break


async def run_main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(signal_handler, nursery.cancel_scope)
        try:
            await pyfuse3.main()
        except trio.Cancelled:
            pass
        except Exception:
            logger.error(f"Unhandled exception", exc_info=True)
            raise
        finally:
            nursery.cancel_scope.cancel()


def exit_hook():
    logger.info("Exiting...")
    pyfuse3.close(unmount=True)


def main():
    try:
        options, foreground, mountpoint, listings = parse_args(sys.argv[1:])
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        print(short_usage, file=sys.stderr,)
        sys.exit(1)

    faulthandler.enable()
    logging.basicConfig(
        level=logging.INFO,
        # format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
        format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger.info("Starting listfs...")

    listfs_options, other_options = transform_user_options(options)
    fuse_options = get_fuse_options(other_options)

    logger.debug(json.dumps(asdict(listfs_options)))
    logger.debug(json.dumps(list(fuse_options)))
    for listing in listings:
        logger.debug(json.dumps(listing))
    logger.debug(json.dumps(mountpoint))

    # Increased load performance 26% on my computer
    g0, g1, g2 = gc.get_threshold()
    gc.set_threshold(max(g0, 50_000), g1 * 5, g2 * 10)

    try:
        operations = ListFS(listfs_options)
        load_all_listings(listings, operations)
    except KeyboardInterrupt:
        logger.info("Exiting due to keyboard interrupt")
        sys.exit(1)

    gc.set_threshold(1, 1, 1)
    operations.pack_memory()
    re.purge()
    logger.info("Garbage collecting...")
    gc.collect()

    try:
        # Release memory on Linux
        import ctypes
        libc = ctypes.CDLL("libc.so.6")
        logger.info("Trimming memory...")
        libc.malloc_trim(0)
        logger.info("Memory trimmed")
    except (OSError, AttributeError) as e:
        logger.info("Memory not trimmed")

    gc.set_threshold(g0, g1, g2)

    logger.info("Mounting...")
    pyfuse3.init(operations, mountpoint, fuse_options)
    logger.info("Mounted.")
    if not foreground:
        daemonize()

    atexit.register(exit_hook)
    try:
        trio.run(run_main, restrict_keyboard_interrupt_to_checkpoints=True)
    except Exception:
        logger.error("Error during FUSE main loop", exc_info=True)


if __name__ == "__main__":
    main()
