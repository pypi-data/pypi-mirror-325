import filecmp
import os
import random
import shutil
import socket
import tempfile
import time
import unittest
import uuid
import zipfile
from hashlib import md5
from http.server import HTTPServer, ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread

from python_download_manager import DownloadManager
from python_download_manager._callbacks import UnpackArchive
from python_download_manager._consts import KB, MB
from python_download_manager._database import DatabaseManager
from python_download_manager._typehint import StrPath

from tests.file_server import ThreadingTestFileServer


class ServerThread(Thread):

    def __init__(self, server: HTTPServer):
        super().__init__()
        self.server = server

    def run(self) -> None:
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()


class TestDownloadManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 存放所有测试文件用的临时目录
        temp_dir_name = tempfile.mkdtemp(prefix=f"{cls.__name__}-")
        cls.temp_dir = Path(temp_dir_name)
        # 存放随机测试文件的目录
        cls.file_dir = cls.temp_dir / "files"
        cls.file_dir.mkdir()
        # 文件服务器
        cls.ip = "127.0.0.1"
        cls.port = random.randint(49152, 65535)
        cls.server = ThreadingTestFileServer(cls.ip, cls.port, cls.file_dir)

        # 随机大文件的下载地址
        cls.large_file_urls = []
        # 随机大文件的md5
        cls.large_file_md5s = {}
        # 生成随机文件，用于下载测试
        print("正在生成测试用大文件...")
        for i in range(10):
            file_name = uuid.uuid4().hex
            file_path = cls.file_dir / file_name
            cls.large_file_urls.append(f"http://{cls.ip}:{cls.port}/{file_name}")
            with open(file_path, "wb") as fp:
                content = random.randbytes(random.randint(4 * MB, 32 * MB))
                fp.write(content)
                file_md5 = md5(content)
                cls.large_file_md5s[file_name] = file_md5.hexdigest()

        print("正在生成测试用小文件...")
        # 随机小文件的下载地址
        cls.small_file_urls = []
        # 随机小文件的md5
        cls.small_file_md5s = {}
        # 生成随机文件，用于下载测试
        print("正在生成测试用小文件...")
        for i in range(10):
            file_name = uuid.uuid4().hex
            file_path = cls.file_dir / file_name
            cls.small_file_urls.append(f"http://{cls.ip}:{cls.port}/{file_name}")
            with open(file_path, "wb") as fp:
                content = random.randbytes(random.randint(16 * KB, 64 * KB))
                fp.write(content)
                file_md5 = md5(content)
                cls.small_file_md5s[file_name] = file_md5.hexdigest()

        print("正在生成测试用zip文件")
        cls.archive_source_dir = cls.temp_dir / "archive_source"
        cls.archive_source_dir.mkdir()
        cls.test_zipfile_path = cls.file_dir / "test.zip"
        zfp = zipfile.ZipFile(cls.test_zipfile_path, "w")
        for i in range(5):
            # 生成待压缩的文件
            archive_file_path: Path = cls.archive_source_dir / uuid.uuid4().hex
            archive_file_path.write_bytes(
                random.randbytes(random.randint(16 * KB, 64 * KB))
            )
            # 将文件添加到压缩包
            zfp.write(
                archive_file_path, archive_file_path.relative_to(cls.archive_source_dir)
            )
        zfp.close()
        # 记录压缩文件md5
        zipfile_md5 = md5(cls.test_zipfile_path.read_bytes())
        cls.small_file_md5s[cls.test_zipfile_path.name] = zipfile_md5.hexdigest()
        # 添加压缩文件的下载链接
        cls.small_file_urls.append(f"http://{cls.ip}:{cls.port}/test.zip")

    @classmethod
    def tearDownClass(cls):
        # 移除测试目录及里面的所有内容
        cls.server.stop()
        shutil.rmtree(cls.temp_dir)

    def setUp(self):
        # 单次测试的临时存储目录
        self.test_dir = self.temp_dir / f"test-{time.time_ns()}"
        self.test_dir.mkdir()
        # 初始化下载管理器
        self.download_manager = DownloadManager(self.test_dir, with_progress=True)
        # 下载文件的保存目录
        self.save_dir = self.test_dir / "download"
        self.save_dir.mkdir()

    def tearDown(self):
        # 校验下载后文件的校验值
        for file in self.save_dir.iterdir():
            self.assertGreater(file.stat().st_size, 0, "File is Empty.")
            if file.name in self.large_file_md5s:
                source_file_md5 = self.large_file_md5s[file.name]
            elif file.name in self.small_file_md5s:
                source_file_md5 = self.small_file_md5s[file.name]
            else:
                raise RuntimeError(f"Unkown file {file.name}")
            downloaded_file_md5 = md5(file.read_bytes())
            self.assertEqual(
                downloaded_file_md5.hexdigest(), source_file_md5, "Checksum error"
            )
        self.download_manager.close()
        shutil.rmtree(self.test_dir)

    def test_init_(self):
        db_file = self.test_dir / DatabaseManager.DB_FILENAME
        self.assertTrue(db_file.exists(), "The database file should exist.")
        self.assertRaises(
            RuntimeError,
            DownloadManager,
            "The RuntimeError should be raised when new DownloadManager twice or more.",
        )

    def test_open_another(self):
        # 关闭当前实例
        self.download_manager.close()
        # 重新打开
        another_db_dir = self.test_dir / "another"
        new_download_manager = DownloadManager(another_db_dir)
        # 判断新实例的数据库文件是否存在
        another_db_file = another_db_dir / DatabaseManager.DB_FILENAME
        self.assertTrue(another_db_file.exists(), "The another db file should exist.")
        new_download_manager.close()

    def test_download_large_file(self):
        """测试下载"""
        # 添加下载任务
        for download_url in self.large_file_urls:
            self.download_manager.add_download_task(
                download_url, save_dir=self.save_dir
            )
        # 开始下载
        self.download_manager.start()
        # 等待下载完成
        completed_tasks = self.download_manager.wait()
        self.assertEqual(
            len(completed_tasks),
            len(self.large_file_urls),
            "len(completed_task) should equal len(large_file_urls)",
        )

    def test_download_small_file(self):
        # 添加下载任务
        for download_url in self.small_file_urls:
            self.download_manager.add_download_task(
                download_url, save_dir=self.save_dir
            )
        # 开始下载
        self.download_manager.start()
        # 等待下载完成
        completed_tasks = self.download_manager.wait()
        self.assertEqual(
            len(completed_tasks),
            len(self.small_file_urls),
            "len(completed_task) should equal len(small_file_urls)",
        )

    def test_download_small_and_zipfile_then_unpack(self):
        unpack_dir = self.test_dir / "unpacked"
        # 添加下载任务
        for download_url in self.small_file_urls:
            self.download_manager.add_download_task(
                download_url,
                save_dir=self.save_dir,
                callbacks=[UnpackArchive(unpack_dir)],
            )
        # 开始下载
        self.download_manager.start()
        self.download_manager.wait()
        # 检查较解压后的文件是否和源文件一致
        comparison = filecmp.dircmp(self.archive_source_dir, unpack_dir)
        self.assertEqual(
            len(comparison.diff_files),
            0,
            "Some files have been changed after unpacking.",
        )
        self.assertEqual(len(comparison.funny_files), 0, "It's not funny at all.")

    def test_download_when_downloading(self):
        """测试在有正在下载的任务时添加新的任务"""
        # 首先添加前5个任务
        for i in range(5):
            self.download_manager.add_download_task(
                self.large_file_urls[i], save_dir=self.save_dir
            )
        # 开始下载
        self.download_manager.start()
        # 继续添加剩下的任务
        for url in self.large_file_urls[5:]:
            self.download_manager.add_download_task(url, save_dir=self.save_dir)
        # 启动后续添加的下载任务
        self.download_manager.start()
        # 等待下载完成
        completed_tasks = self.download_manager.wait()
        self.assertEqual(
            len(completed_tasks),
            len(self.large_file_urls),
            "len(completed_task) should equal len(large_file_urls)",
        )

    def test_delete_completed_tasks(self):
        # 执行下载任务
        for url in self.small_file_urls:
            self.download_manager.add_download_task(url, save_dir=self.test_dir)
        self.download_manager.start()
        completed_tasks = self.download_manager.wait()
        # 删除完成的下载记录
        deleted_tasks = self.download_manager.delete_completed_tasks()
        # 判断删除的数量是否与下载记录的数量相等
        self.assertEqual(len(completed_tasks), len(deleted_tasks))

    def test_delete_completed_tasks_with_args(self):
        # 执行下载任务
        for url in self.small_file_urls:
            self.download_manager.add_download_task(url, save_dir=self.test_dir)
        self.download_manager.start()
        completed_tasks = self.download_manager.wait()
        # 随机挑选几个下载记录来删除
        random_task = random.choices(completed_tasks, k=5)
        task_ids = {task.id for task in random_task}
        deleted_tasks = self.download_manager.delete_completed_tasks(task_ids)
        # 判断删除的数量是否与随机选出来的记录的数量相等
        self.assertEqual(len(task_ids), len(deleted_tasks))

    def test_delete_deleted_tasks(self):
        # 添加下载任务
        for url in self.small_file_urls:
            self.download_manager.add_download_task(url, save_dir=self.test_dir)
        # 将下载任务放入回收站
        tasks = self.download_manager.delete_download_tasks()
        # 删除回收站内的所有任务
        deleted_tasks = self.download_manager.delete_deleted_tasks()
        # 判断删除的任务是否与回收站内的任务数量相等
        self.assertEqual(len(tasks), len(deleted_tasks))

    def test_delete_deleted_tasks_with_args(self):
        # 添加下载任务
        for url in self.small_file_urls:
            self.download_manager.add_download_task(url, save_dir=self.test_dir)
        # 将下载任务放入回收站
        tasks = self.download_manager.delete_download_tasks()
        # 随机选出若干个回收站内的任务进行删除
        random_tasks = random.choices(tasks, k=5)
        task_ids = {task.id for task in random_tasks}
        deleted_tasks = self.download_manager.delete_deleted_tasks(task_ids)
        # 判断删除的任务是否与随机选出来的的任务数量相等
        self.assertEqual(len(task_ids), len(deleted_tasks))

    def test_delete_download_tasks(self):
        # 添加下载任务
        for url in self.small_file_urls:
            self.download_manager.add_download_task(url, save_dir=self.test_dir)
        # 将下载任务放入回收站
        deleted_tasks = self.download_manager.delete_download_tasks()
        # 判断放入回收站内的任务是否和添加的任务数量相等
        self.assertEqual(len(deleted_tasks), len(self.small_file_urls))

    def test_delete_download_tasks_with_args(self):
        # 添加下载任务
        for url in self.small_file_urls:
            self.download_manager.add_download_task(url, save_dir=self.test_dir)
        # 将下载任务放入回收站
        deleted_tasks = self.download_manager.delete_download_tasks()
        # 判断放入回收站内的任务是否和添加的任务数量相等
        self.assertEqual(len(deleted_tasks), len(self.small_file_urls))

    def test_delete_downloading_tasks(self):
        # 添加下载任务
        for url in self.large_file_urls:
            self.download_manager.add_download_task(url, save_dir=self.test_dir)
        # 开始下载
        self.download_manager.start()
        self.download_manager.delete_downloading_tasks()


    def test_delete_downloading_tasks_with_args(self):
        pass

    def test_get_all_download_task(self):
        pass

    def test_get_all_download_task_with_args(self):
        pass

    def test_get_all_downloading_task(self):
        pass

    def test_get_all_downloading_task_with_args(self):
        pass

    def test_get_all_deleted_task(self):
        pass

    def test_get_all_deleted_task_with_args(self):
        pass

    def test_get_all_completed_task(self):
        pass

    def test_get_all_completed_task_args(self):
        pass
