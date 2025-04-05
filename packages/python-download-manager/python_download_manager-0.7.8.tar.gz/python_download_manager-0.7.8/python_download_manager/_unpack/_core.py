import zipfile
from pathlib import Path

import py7zr
from unrar.cffi import rarfile

from ._adapter import RarAdapter, SevenZipAdapter, ZipAdapter
from .._typehint import StrPath


def unpack_archive(filepath: StrPath, unpack_dir: StrPath = None, password: str = None):
    if zipfile.is_zipfile(filepath):
        archive = ZipAdapter(filepath, password)
    elif rarfile.is_rarfile(filepath):
        archive = RarAdapter(filepath, password)
    elif py7zr.is_7zfile(filepath):
        archive = SevenZipAdapter(filepath, password)
    else:
        raise NotImplementedError(f"Unsupport archive type {Path(filepath.suffix)}")
    archive.unpack(unpack_dir)
