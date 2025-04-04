import os
from datetime import datetime
from pathlib import Path
import time
from threading import Event,Lock

from ._filewriter import (
    get_file_writer,
    FileWriter,
    MultiPartFileWriter,
    MutexFileWriter,
    SequenceFileWriter,
)
from .._structures import ThreadSafeDict
from .._typehint import StrPath


class StorageManager:
    """
    1. 用指定的文件写入器写入文件，不指定时用以SequenceFileWriter作为默认写入器
    2. 写入完毕后将文件的最后修改时间设置成response的headers里面指定的值
    """

    file_writer_class = SequenceFileWriter
    __file_writers:dict[StrPath,FileWriter] = ThreadSafeDict()
    __stop_events: dict[StrPath, Event] = ThreadSafeDict()

    @classmethod
    def close(cls, file_path, modify_time: datetime = None):
        file_path = Path(file_path).absolute()
        file_writer = cls.__file_writers.pop(file_path)
        file_writer.close()
        stop_event = cls.__stop_events.pop(file_path)
        stop_event.set()
        if modify_time is not None and file_path.exists():
            cls.update_access_and_modify_time(file_path, modify_time=modify_time)

    @classmethod
    def delete(cls,file_path:StrPath):
        file_path = Path(file_path).absolute()

        if not file_path.exists():
            return
        
        if file_path in cls.__file_writers:
            cls.__file_writers[file_path].close()

        file_path.unlink()

    @classmethod
    def open(
        cls,
        file_path: StrPath,
        file_size: int = 0,
        file_writer_class_name: str = None,
    ) -> str:
        file_path = file_path.absolute()
        if file_writer_class_name not in (
            MultiPartFileWriter.__name__,
            MutexFileWriter.__name__,
            SequenceFileWriter.__name__,
        ):
            file_writer_class_name = SequenceFileWriter.__name__
        file_writer = get_file_writer(file_writer_class_name, file_path, file_size)
        cls.__file_writers[file_path] = file_writer
        cls.__stop_events[file_path] = Event()
        return file_writer_class_name

    @staticmethod
    def update_access_and_modify_time(
        file_path: StrPath, access_time: datetime = None, modify_time: datetime = None
    ):
        if access_time is None:
            access_time = datetime.now()
        if modify_time is None:
            modify_time = datetime.now()
        times = (access_time.timestamp(), modify_time.timestamp())
        os.utime(file_path, times)

    @classmethod
    def write(cls, file_path: StrPath, content: bytes, index: int) -> int:
        if len(content) == 0:
            return 0

        file_path = Path(file_path).absolute()
        file_writer = cls.__file_writers[file_path]

        while not cls.__stop_events[file_path].is_set():
            if file_writer.closed:
                return 0
            written_size = file_writer.write(content, index)
            if written_size == 0:
                time.sleep(0.1)
            else:
                return written_size

        return 0

    @classmethod
    def stop(cls,file_path:StrPath):
        file_path = Path(file_path).absolute()
        cls.__stop_events[file_path].set()