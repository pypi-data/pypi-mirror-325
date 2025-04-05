import math
import unittest

from python_download_manager import _utility
from python_download_manager._consts import KB, MB


class TestUtility(unittest.TestCase):

    def test_get_filename_from_url(self):
        """测试从url中获取文件名"""
        filename = _utility.get_filename_from_url(
            "https://www.sample.com/downlaod/test.mp4"
        )
        self.assertEqual(filename, "test.mp4")

    def test_slice_file(self):
        """测试分割文件块"""
        file_size = 256 * MB
        chunk_size = 16 * MB
        chunks = _utility.slice_file(file_size, chunk_size)
        # 检查文件块数量
        chunk_count = math.ceil(file_size / chunk_size)
        self.assertEqual(len(chunks), chunk_count, "文件块的数量不正确")
        # 检查文件块的边界
        self.assertEqual(chunks[0].start, 0, "第一个文件块的start应当小于等于0")
        self.assertEqual(
            chunks[-1].end, file_size - 1, f"最后一个文件块的end值应当为{file_size - 1}"
        )
        for i in range(len(chunks) - 1):
            self.assertEqual(
                chunks[i].end + 1,
                chunks[i + 1].start,
                "前一个chunk的end+1应当等于后一个chunk的start",
            )

    def test_format_file_size(self):
        """测你大爷，这么简单的功能还能出bug?"""
        formated_2m = _utility.format_file_size(2 * MB)
        self.assertEqual(formated_2m, "2 MB")
        formated_100m100k = _utility.format_file_size(100 * MB + 100 * KB)
        self.assertEqual(formated_100m100k, "100.09765625 MB")
