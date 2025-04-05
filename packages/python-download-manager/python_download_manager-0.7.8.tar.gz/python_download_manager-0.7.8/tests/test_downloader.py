from hashlib import md5
from pathlib import Path
import random
import shutil
import tempfile
import time
import unittest
import uuid

from python_download_manager._consts import KB, MB
from python_download_manager._database import (
    DatabaseManager,
    DownloadTask,
    DownloadingTask,
)
from python_download_manager._task_scheduler._task_downloader import TaskDownloader
from python_download_manager._session_manager import SessionManager
from tests.file_server import ThreadingTestFileServer


class TestDownloader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 存放所有测试文件用的临时目录
        temp_dir_name = tempfile.mkdtemp(prefix=f"{cls.__name__}-")
        cls.temp_dir = Path(temp_dir_name)
        # 存放随机测试文件的目录
        cls.file_dir = cls.temp_dir / "files"
        cls.file_dir.mkdir()
        # 启动文件服务器
        ip = "127.0.0.1"
        port = random.randint(49152, 65535)
        cls.server = ThreadingTestFileServer(ip, port, cls.file_dir)

        # 测试文件
        cls.file_path = cls.file_dir / uuid.uuid4().hex
        content = content = random.randbytes(random.randint(4 * MB, 32 * MB))
        cls.file_md5 = md5(content).hexdigest()
        cls.file_path.write_bytes(content)
        cls.file_url = f"http://{ip}:{port}/{cls.file_path.name}"

        # 初始化会话管理器
        SessionManager.initialize()

    @classmethod
    def tearDownClass(cls):
        cls.server.stop()
        # shutil.rmtree(cls.temp_dir)

    def setUp(self):
        # 单次测试的临时存储目录
        self.test_dir = self.temp_dir / f"test-{time.time_ns()}"
        self.test_dir.mkdir()
        # 初始化数据库
        DatabaseManager.initialize(self.test_dir)
        # 下载文件的保存目录
        self.save_dir = self.test_dir / "download"

    def tearDown(self):
        DatabaseManager.close()
        # shutil.rmtree(self.test_dir)

    def test_download_file(self):
        task = DownloadTask(download_url=self.file_url, save_dir=self.save_dir)
        added_task = DatabaseManager.add_download_task(task)
        with TaskDownloader(task) as downloader:
            downloader.start()
            complete_task = downloader.wait_until_complete()
        # 检查是否正常下载完成
        self.assertIsNotNone(complete_task)
        # 检查文件是否为空
        downloaded_file_size = downloader.task.file_path.stat().st_size
        self.assertNotEqual(downloaded_file_size,0,"Downloaded file is empty.")
        # 检查下载后的文件的md5
        downloaded_file_md5 = md5(downloader.task.file_path.read_bytes()).hexdigest()
        self.assertEqual(downloaded_file_md5,self.file_md5,"Checksum Error.")
        # 检查数据库中是否存在下载记录
        completed_tasks = DatabaseManager.get_all_completed_download_task(task_ids=[downloader.task.id])
        self.assertEqual(len(completed_tasks),1,"The CompletedDownloadTask doesn't exist in database.")

