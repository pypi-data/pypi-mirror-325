import logging
import random
import tempfile
import time
import unittest
import uuid
from concurrent import futures
from pathlib import Path

import psutil

from python_download_manager import _utility
from python_download_manager._consts import MB, GB
from python_download_manager._storage._filewriter import (
    MultiPartFileWriter,
    MutexFileWriter,
    SequenceFileWriter,
)

logger = logging.getLogger(__name__)


class TestWriteAmplification(unittest.TestCase):
    """测试各个文件写入器的写放大比率
    使用方法：每个测试用例都会向临时目录写入一个1G大小的随机文件，
    运行测试前用crystal disk info等工具查看临时目录所在的硬盘的当前写入量
    运行测试后再刷新软件界面查看运行测试后实际产生的写入量
    注意：不要同时运行多个测试用例
    """

    def setUp(self):
        # 测试文件路径
        self.test_file_path = Path(tempfile.gettempdir(), f"test_file_{uuid.uuid4().hex}")
        # 测试文件大小，块大小，分块列表
        self.file_size = 1 * GB
        self.chunk_size = 4 * MB
        self.chunks = _utility.slice_file(self.file_size, self.chunk_size)

        # 测试开始前的写入量
        self.befor_write_bytes = psutil.disk_io_counters().write_bytes

    def tearDown(self):
        # 等待30秒，等系统记录完写入量
        time.sleep(30)
        # 写入完成后的写入量
        self.after_write_bytes = psutil.disk_io_counters().write_bytes
        # 写入前后的写入量差值应当比文件大小大
        write_count = self.after_write_bytes - self.befor_write_bytes
        self.assertGreaterEqual(
            write_count,
            self.file_size,
            f"写入量不正确,"
            f"文件大小为{_utility.format_file_size(self.file_size)},"
            f"检测到的写入量为{_utility.format_file_size(write_count)}",
        )
        real_write_count = self.after_write_bytes - self.befor_write_bytes
        print(
            f"文件大小为{_utility.format_file_size(self.file_size)} ",
            f"实际写入量为{_utility.format_file_size(real_write_count)} ",
            f"写放大为{real_write_count / self.file_size}",
        )
        self.test_file_path.unlink(missing_ok=True)

    def test_multipar_file_writer(self):
        """测试多段文件写入器"""
        # 文件写入器
        file_writer = MultiPartFileWriter(self.test_file_path, self.file_size)
        # 将文件块列表打乱，模拟更复杂的情况
        random.shuffle(self.chunks)
        # 启用多线程写入文件块
        self._write_random_content_with_multi_thread(file_writer, self.chunks)
        file_writer.close()

    def test_mutex_file_writer(self):
        """测试互斥文件写入器"""
        # 文件写入器
        file_writer = MutexFileWriter(self.test_file_path, self.file_size)
        # 将文件块列表反转，模拟最差的文件写入顺序
        self.chunks.reverse()
        # 启用多线程写入文件块
        self._write_random_content_with_multi_thread(file_writer, self.chunks)
        file_writer.close()

    def test_sequence_file_writer(self):
        """测试顺序文件写入器"""
        # 文件写入器
        file_writer = SequenceFileWriter(self.test_file_path, self.file_size)
        # 启用多线程写入文件块
        self._write_random_content_with_multi_thread(file_writer, self.chunks)
        file_writer.close()

    def _write_random_content_with_multi_thread(self, file_writer, chunks):
        logger.debug(f"writing random content. writer:{file_writer.__class__.__name__},")
        with futures.ThreadPoolExecutor(max_workers=5) as executor:
            submitted_tasks = [
                executor.submit(
                    file_writer.write, random.randbytes(chunk.end + 1 - chunk.start), chunk.start
                )
                for chunk in self.chunks
            ]
            futures.as_completed(submitted_tasks)
