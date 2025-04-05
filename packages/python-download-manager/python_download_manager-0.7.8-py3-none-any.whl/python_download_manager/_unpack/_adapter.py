import os
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

from py7zr import SevenZipFile
from unrar.cffi.rarfile import RarFile

from .._typehint import StrPath


class ArchiveAdapter(ABC):

    @abstractmethod
    def __init__(self, filepath: StrPath, pwd: str = None):
        self.filepath = filepath
        self.pwd = pwd
        self._file = None

    def close(self):
        if self._file is not None and hasattr(self._file, "close"):
            self._file.close()
            self._file = None

    @abstractmethod
    def unpack(self, path):
        raise NotImplementedError

    def __enter__(self):
        return self

    def __exit__(self, error_type, error_value, traceback):
        self.close()
        return False


class RarAdapter(ArchiveAdapter):
    def __init__(self, filepath: StrPath, pwd: str = None):
        super().__init__(filepath, pwd)
        self._file = RarFile(filepath, pwd=pwd)

    def unpack(self, path: StrPath = None):
        unpack_path = Path(path or ".")
        for info in reversed(self._file.infolist()):
            out_path = unpack_path / info.filename
            if info.is_dir():
                # 创建文件夹
                out_path.mkdir(exist_ok=True)
            else:
                # 读取压缩包内数据并写入磁盘
                rarfp = self._file.open(info)
                fp = open(out_path, "wb")
                while True:
                    # 每次只读取最多4MB数据
                    content = rarfp.read(4 * 1024 ** 2)
                    if len(content) == 0:
                        break
                    fp.write(content)
                    fp.flush()
                rarfp.close()
                fp.close()
                # 同步文件修改时间
                atime = datetime.now().timestamp()
                mtime = datetime(*info.date_time).timestamp()
                os.utime(out_path, (atime, mtime))


class SevenZipAdapter(ArchiveAdapter):

    def __init__(self, filepath: StrPath, pwd: str = None):
        super().__init__(filepath, pwd)
        self._file = SevenZipFile(filepath, password=pwd)

    def unpack(self, path: StrPath = None):
        self._file.extractall(path)


class ZipAdapter(ArchiveAdapter):

    def __init__(self, filepath: StrPath, pwd: str = None):
        super().__init__(filepath, pwd)
        self._file = ZipFile(filepath)

    def unpack(self, path: StrPath = None):
        if self.pwd:
            self._file.extractall(path, pwd=self.pwd.encode("utf-8"))
        else:
            self._file.extractall(path)
