import filecmp
import shutil
import tempfile
import unittest
from pathlib import Path

from python_download_manager._unpack._adapter import (
    RarAdapter,
    SevenZipAdapter,
    ZipAdapter,
)


class TestUnpack(unittest.TestCase):
    def setUp(self):
        print("parent setUP")
        self.test_output_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.test_output_dir)

    def compare_unpack_result(self, unpack_dir, source_dir):
        # compare
        comparison = filecmp.dircmp(unpack_dir, source_dir)
        self.assertEqual(
            len(comparison.diff_files),
            0,
            "Some files have been changed after unpacking.",
        )
        self.assertEqual(len(comparison.funny_files), 0, "It is not funny at all!")


class TestRarFile(TestUnpack):

    def test_unpack(self):
        # unpack
        rar = RarAdapter("tests/sample-rar-files/sample.rar")
        rar.unpack(self.test_output_dir)
        # source_dir
        source_dir = "tests/sample-rar-files/source"
        # compare
        self.compare_unpack_result(self.test_output_dir, source_dir)

    def test_unpack_with_pwd(self):
        # unpack
        rar = RarAdapter("tests/sample-rar-files/sample-pwd=test.rar", pwd="test")
        rar.unpack(self.test_output_dir)
        # source_dir
        source_dir = "tests/sample-rar-files/source"
        # compare
        self.compare_unpack_result(self.test_output_dir, source_dir)


class TestSevenZipFile(TestUnpack):

    def test_unpack(self):
        # unpack
        seven_zip = SevenZipAdapter("tests/sample-7z-files/sample.7z")
        seven_zip.unpack(self.test_output_dir)
        # source_dir
        source_dir = "tests/sample-7z-files/source"
        # compare
        self.compare_unpack_result(self.test_output_dir, source_dir)

    def test_unpack_with_pwd(self):
        # unpack
        seven_zip = SevenZipAdapter("tests/sample-7z-files/sample-pwd=test.7z", pwd="test")
        seven_zip.unpack(self.test_output_dir)
        # source_dir
        source_dir = "tests/sample-7z-files/source"
        # compare
        self.compare_unpack_result(self.test_output_dir, source_dir)


class TestZipFile(TestUnpack):

    def test_unpack(self):
        # unpack
        zipf = ZipAdapter("tests/sample-zip-files/sample.zip")
        zipf.unpack(self.test_output_dir)
        # source_dir
        source_dir = "tests/sample-zip-files/source"
        # compare
        self.compare_unpack_result(self.test_output_dir, source_dir)

    def test_unpack_with_pwd(self):
        # unpack
        zipf = ZipAdapter("tests/sample-zip-files/sample-pwd=test.zip", pwd="test")
        zipf.unpack(self.test_output_dir)
        # source_dir
        source_dir = "tests/sample-zip-files/source"
        # compare
        self.compare_unpack_result(self.test_output_dir, source_dir)
