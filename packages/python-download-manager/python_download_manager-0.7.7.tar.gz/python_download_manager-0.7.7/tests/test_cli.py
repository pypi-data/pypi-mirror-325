import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from python_download_manager import _cli


class TestCli(unittest.TestCase):
    def setUp(self):
        # 临时目录
        self.temp_dir = Path(tempfile.gettempdir(), "pdm.TestCli")
        self.temp_dir.mkdir(exist_ok=True)
        # 修改cli的工作目录
        _cli._work_dir = self.temp_dir
        # python解释器的位置
        self.python = ".venv/Scripts/python"

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_download(self):
        args = [
            self.python,
            "-m",
            "python_download_manager",
            "download",
            "https://dldir1.qq.com/qqfile/qq/PCQQ9.7.17/QQ9.7.17.29225.exe",
            "-d",
            self.temp_dir
        ]
        subprocess.run(args)

    def test_batch(self):
        args = [
            self.python,
            "-m",
            "python_download_manager",
            "batch",
            "https://dldir1.qq.com/qqfile/qq/PCQQ9.7.17/QQ9.7.17.29225.exe",
            "https://dtapp-pub.dingtalk.com/dingtalk-desktop/win_downloader/20241127/dingtalk_downloader.exe",
            "https://kimi-img.moonshot.cn/prod-chat-kimi/kimi/kimi-desktop-windows-x86.exe",
            "https://www.runoob.com/wp-content/uploads/2016/04/docker01.png",
            "https://down.sandai.net/thunder11/XunLeiWebSetup12.1.2.2662xl11.exe",
            "-d",
            self.temp_dir
        ]
        subprocess.run(args)
