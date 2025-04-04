import random
import tempfile
import unittest
import uuid
from concurrent import futures
from hashlib import md5
from pathlib import Path

from python_download_manager import _utility
from python_download_manager._consts import MB
from python_download_manager._storage._filewriter import (
    MultiPartFileWriter,
    MutexFileWriter,
    SequenceFileWriter,
)


class BaseTestFileWriter(unittest.TestCase):
    def setUp(self):
        # 测试文件路径
        self.test_file_path = Path(tempfile.gettempdir(), f"test_file_{uuid.uuid4().hex}")
        # 测试文件的md5
        self.test_file_md5 = md5()
        # 用于测试的文件，大小在16-256MB之间，文件块大小为4到16MB之间
        self.file_size = random.randrange(16 * MB, 256 * MB)
        self.chunk_size = random.randrange(4 * MB, 16 * MB)
        self.chunks = _utility.slice_file(self.file_size, self.chunk_size)

    def tearDown(self):
        self.test_file_path.unlink(missing_ok=True)

    def _write_random_content_with_multi_thread(self, file_writer, chunks):
        with futures.ThreadPoolExecutor(max_workers=5) as executor:
            submitted_tasks = []
            for chunk in chunks:
                random_content = random.randbytes(self.chunk_size)
                self.test_file_md5.update(random_content)
                submitted_task = executor.submit(
                    file_writer.write, random_content, chunk.start
                )
                submitted_tasks.append(submitted_task)
            futures.as_completed(submitted_tasks)


class TestMultiPartFileWriter(BaseTestFileWriter):

    def test_normal_write(self):
        """测试正常写入文件"""
        file_writer = MultiPartFileWriter(self.test_file_path, self.file_size)
        # 空白文件应当存在
        self.assertTrue(self.test_file_path.exists(), "empty test file should exist")
        # 空白文件应当预分配和文件大小一样的空间
        self.assertEqual(
            self.test_file_path.stat().st_size,
            self.file_size,
            f"test file size should be {self.file_size},but {self.test_file_path.stat().st_size}",
        )
        # 用于缓存的目录应当存在
        self.assertTrue(file_writer.cache_dir.exists(), "cache dir should exist")
        # 模拟多线程写入文件块
        self._write_random_content_with_multi_thread(file_writer, self.chunks)
        # 关闭并保存文件
        file_writer.close()
        # 保存后，缓存目录应当被删除
        self.assertFalse(
            file_writer.cache_dir.exists(),
            "The cache dir should be removed after the file is written",
        )
        # 校验文件md5
        written_file_md5 = md5()
        written_file_md5.update(self.test_file_path.read_bytes())
        self.assertEqual(
            self.test_file_md5.hexdigest(),
            written_file_md5.hexdigest(),
            "md5 test fail",
        )


class TestMutexFileWriter(BaseTestFileWriter):
    def test_normal_write(self):
        """测试正常写入文件"""
        file_writer = MutexFileWriter(self.test_file_path, self.file_size)
        # 空白文件应当存在
        self.assertTrue(self.test_file_path.exists(), "empty test file should exist")
        # 空白文件应当预分配和文件大小一样的空间
        self.assertEqual(
            self.test_file_path.stat().st_size,
            self.file_size,
            f"test file size should be {self.file_size},but {self.test_file_path.stat().st_size}",
        )
        # 模拟多线程写入文件块
        self._write_random_content_with_multi_thread(file_writer, self.chunks)
        # 关闭并保存文件
        file_writer.close()
        # 校验文件md5
        written_file_md5 = md5()
        written_file_md5.update(self.test_file_path.read_bytes())
        self.assertEqual(
            self.test_file_md5.hexdigest(),
            written_file_md5.hexdigest(),
            "md5 test fail",
        )


class TestSequenceFileWriter(BaseTestFileWriter):
    def test_normal_write(self):
        """测试正常写入文件"""
        file_writer = SequenceFileWriter(self.test_file_path, self.file_size)
        # 空白文件应当存在
        self.assertTrue(self.test_file_path.exists(), "empty test file should exist")
        # 模拟多线程写入文件块
        self._write_random_content_with_multi_thread(file_writer, self.chunks)
        # 关闭并保存文件
        file_writer.close()
        # 校验文件md5
        written_file_md5 = md5()
        written_file_md5.update(self.test_file_path.read_bytes())
        self.assertEqual(
            self.test_file_md5.hexdigest(),
            written_file_md5.hexdigest(),
            "md5 test fail",
        )
