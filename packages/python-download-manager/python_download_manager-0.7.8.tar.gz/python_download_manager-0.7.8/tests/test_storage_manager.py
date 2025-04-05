import concurrent.futures
import random
import shutil
import tempfile
import unittest
import uuid
from concurrent.futures import ThreadPoolExecutor
from hashlib import md5
from pathlib import Path

from python_download_manager._consts import MB
from python_download_manager._storage import StorageManager


class TestStorageManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def write_random(self, file_path) -> (str, str):
        # 在存储管理器中打开文件
        StorageManager.open(file_path)
        # 随机源文件的md5
        source_md5 = md5()
        # 写入随机内容
        index = 0
        for i in range(random.randint(5, 10)):
            random_content = random.randbytes(1 * MB)
            StorageManager.write(file_path, random_content, index)
            source_md5.update(random_content)
            index += len(random_content)
        # 关闭文件
        StorageManager.close(file_path)
        return file_path, source_md5.hexdigest()

    def test_one(self):
        file_path, source_md5 = self.write_random(
            self.temp_dir / uuid.uuid4().hex
        )
        # 验证写入的内容是否正确
        written_md5 = md5()
        with open(file_path, "rb") as fp:
            written_md5.update(fp.read())
        self.assertEqual(
            written_md5.hexdigest(), source_md5, "Checksum Error"
        )

    def test_multi_thread(self):
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(
                    self.write_random,
                    Path(self.temp_dir, uuid.uuid4().hex),
                )
                for _ in range(10)
            ]
            for future in concurrent.futures.as_completed(futures):
                file_path, source_md5 = future.result()
                written_md5 = md5()
                with open(file_path, "rb") as fp:
                    written_md5.update(fp.read())
                self.assertEqual(
                    written_md5.hexdigest(), source_md5, "Checksum Error"
                )
