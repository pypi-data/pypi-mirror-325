import os
from datetime import datetime
from pathlib import Path
from typing import Union

from .filewriter import (
    get_file_writer,
    MultiPartFileWriter,
    MutexFileWriter,
    SequenceFileWriter,
)


class StorageManager:
    """
    1. 用指定的文件写入器写入文件，不指定时用以SequenceFileWriter作为默认写入器
    2. 写入完毕后将文件的最后修改时间设置成response的headers里面指定的值
    """
    file_writer_class = SequenceFileWriter
    __file_writers = {}

    @classmethod
    def close(cls, file_path, modify_time: datetime = None):
        file_path = Path(file_path).absolute()
        file_writer = cls.__file_writers.pop(file_path)
        file_writer.close()
        if modify_time is not None:
            cls.update_access_and_modify_time(file_path, modify_time=modify_time)

    @classmethod
    def open(
            cls,
            file_path: Union[str, Path],
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
        return file_writer_class_name

    @staticmethod
    def update_access_and_modify_time(file_path: Union[str, Path], access_time: datetime = None,
                                      modify_time: datetime = None):
        if access_time is None:
            access_time = datetime.now()
        if modify_time is None:
            modify_time = datetime.now()
        times = (access_time.timestamp(), modify_time.timestamp())
        os.utime(file_path, times)

    @classmethod
    def write(cls, file_path: Union[str, Path], content: bytes, index: int) -> int:
        file_path = Path(file_path).absolute()
        file_writer = cls.__file_writers[file_path]
        return file_writer.write(content, index)
