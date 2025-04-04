import concurrent.futures
import random
import time
import unittest
from concurrent.futures import ThreadPoolExecutor

from python_download_manager import _utility
from python_download_manager._consts import MB
from python_download_manager._database import DownloadTask, Chunk
from python_download_manager._progress import TqdmProgressManager


class TestTqdmProgressManager(unittest.TestCase):

    def setUp(self):
        TqdmProgressManager.initialize()
        self.download_tasks = []
        for i in range(20):
            task = DownloadTask(
                id=i,
                download_url="test_url",
                file_writer_class_name="None",
                filename=f"file_{i:02d}",
                headers={"Content-Length":str(random.randint(16, 128) * MB)},
            )
            self.download_tasks.append(task)

    def mock_download_chunk(self, chunk: Chunk, task: DownloadTask):
        # 暂停若干秒，模仿下载耗时
        time.sleep(random.random())
        TqdmProgressManager.update(task.id, chunk.size)

    def mock_download_chunks(self, task: DownloadTask):
        with ThreadPoolExecutor(max_workers=5) as chunk_executor:
            futures = []
            for chunk in _utility.slice_file(task.file_size, 4 * MB):
                future = chunk_executor.submit(self.mock_download_chunk, chunk, task)
                futures.append(future)
            concurrent.futures.wait(futures)
        TqdmProgressManager.unregister(task.id)

    def mock_download_tasks(self, tasks: list[DownloadTask]):
        with ThreadPoolExecutor(max_workers=5) as task_executor:
            futures = []
            for task in tasks:
                TqdmProgressManager.register(task.id, task.file_size)
                future = task_executor.submit(self.mock_download_chunks, task)
                futures.append(future)
            concurrent.futures.wait(futures)

    def test_one(self):
        self.mock_download_tasks(random.choices(self.download_tasks))

    def test_multi_thread(self):
        self.mock_download_tasks(self.download_tasks)

    def test_set_total(self):
        for task in self.download_tasks:
            TqdmProgressManager.register(task.id, 0)
        for task in self.download_tasks:
            TqdmProgressManager.set_total(task.id, task.file_size)

    def test_set_progress(self):
        for task in self.download_tasks:
            TqdmProgressManager.register(task.id, task.file_size)
        for task in self.download_tasks:
            TqdmProgressManager.set_progress(task.id, task.file_size)
