import logging
import shutil
import subprocess
import sys
import threading
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

logger = logging.getLogger(__name__)


class FileWriter(ABC):
    file_path: Union[str, Path]
    file_size: int

    @abstractmethod
    def write(self, content: bytes, index: int) -> int:
        """写入内容"""
        pass

    @abstractmethod
    def close(self):
        """关闭将保存文件"""
        pass

    def _create_empty_file(self, file_size: int):
        """创建空文件，并预分配存储空间"""
        if not self.file_path.parent.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if sys.platform == "win32":
            command = (
                "fsutil",
                "file",
                "createnew",
                str(self.file_path),
                str(file_size),
            )
        else:
            command = (
                "dd",
                "if=/dev/zero",
                f"of={self.file_path}",
                "bs=1",
                "count=0",
                f"seek={file_size}",
            )
        logger.debug(f"execute command:{' '.join(command)}")
        completed_process = subprocess.run(command, stdout=subprocess.PIPE)
        try:
            output = completed_process.stdout.decode("ansi")
        except LookupError:
            output = completed_process.stdout.decode("utf-8")
        logger.debug(f"command output:{output}")


class MultiPartFileWriter(FileWriter):
    """多段文件写入器
    写放大比率为1，写入1GB的文件会产生2GB的实际写入量
    将每次写入的内容缓存成磁盘上的一个小文件，
    调用close方法时将所有小文件合并成最终要写入的文件
    """

    def __init__(self, file_path: Union[str, Path], file_size: int = 0):
        self.file_path = Path(file_path)
        self.file_size = file_size
        # 创建空文件并预分配空间
        if not self.file_path.exists():
            self._create_empty_file(self.file_size)
        # 创建临时缓存目录
        self.cache_dir = (
                self.file_path.parent / f".{self.file_path.stem}.{file_size}.cache"
        )
        self.cache_dir.mkdir(exist_ok=True)

    def write(self, content: bytes, index: int) -> int:
        with open(self.cache_dir / str(index), "wb") as fp:
            return fp.write(content)

    def close(self):
        # 遍历出缓存文件夹下的所有文件
        cache_files = [file for file in self.cache_dir.iterdir()]
        # 将文件按文件名正序排序
        cache_files.sort(key=lambda p: int(p.name))
        # 将缓存文件合并成最终结果
        with open(self.file_path, "rb+") as fp:
            for cache_file in cache_files:
                fp.write(cache_file.read_bytes())
        # 删除缓存文件
        shutil.rmtree(self.cache_dir)


class MutexFileWriter(FileWriter):
    """互斥文件写入器
    最好的情况(所有文件块按顺序写入)，写放大比率为1
    一般多线程乱序写入的情况下，写放大的比率为2以上
    通过加锁来保证同一时刻只有一个线程在写入
    """

    def __init__(self, file_path: str, file_size: int):
        self.file_path = Path(file_path)
        self.file_size = file_size
        # 要写入的文件不存在时创建并预分配相应大小的空间
        if not self.file_path.exists():
            self._create_empty_file(self.file_size)
        # 打开要写入的文件
        self.__file = open(self.file_path, "rb+")
        # 线程锁，用于保证同一时刻只有一个线程在执行写入操作
        self.__file_lock = threading.Lock()

    def write(self, content: bytes, index: int) -> int:
        with self.__file_lock:
            self.__file.seek(index)
            bytes_count = self.__file.write(content)
            self.__file.flush()
        return bytes_count

    def close(self):
        self.__file.close()


class SequenceFileWriter(FileWriter):
    """顺序文件写入器
    没有写放大，写入1GB的文件只会产生1GB的写入量
    会按顺序写入文件，如果写的内容的位置在当前文件指针之后，会产生阻塞，
    直到其他线程将写入内容，将文件指针移动到相应的位置。
    在多线程的情况下，请尽量保证文件是按顺序写入的，否则有可能会产生死锁
    在单线程写入的情况下，务必要保证每次写入的内容是连续的，否则会一直处于阻塞状态。
    """

    def __init__(self, file_path: Union[str, Path], file_size: int = 0):
        self.file_path = Path(file_path)
        self.file_size = file_size
        if not self.file_path.exists():
            self._create_empty_file(0)
        # 打开文件
        self.__file = open(self.file_path, "rb+")
        # 当前文件指针位置
        self.current_index = self.file_path.stat().st_size
        self.__file_lock = threading.Lock()

    def write(self, content: bytes, index: int) -> int:
        while self.current_index < index:
            time.sleep(0.01)
        with self.__file_lock:
            self.__file.seek(index)
            bytes_count = self.__file.write(content)
            self.__file.flush()
            self.current_index = max(self.current_index, index + len(content))
        return bytes_count

    def close(self):
        self.__file.close()


def get_file_writer(
        class_name: str, file_path: Union[str, Path], file_size: int = 0
) -> FileWriter:
    module = sys.modules[__name__]
    file_writer_class = getattr(module, class_name)
    return file_writer_class(file_path=file_path, file_size=file_size)
