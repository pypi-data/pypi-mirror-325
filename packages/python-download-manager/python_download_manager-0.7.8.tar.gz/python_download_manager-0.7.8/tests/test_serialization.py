import unittest
from datetime import datetime
from pathlib import Path

from python_download_manager import _serialization
from python_download_manager._callbacks import UnpackArchive


@_serialization.serializable
class SampleClass:
    def __init__(
            self,
            # origin types
            int_var,
            float_var=2.0,
            str_var="3",
            list_var=[4, 5, 6],
            dict_var={"7": 7, "8": 8, "9": 9},
            # custom types
            bytes_var=b"test",
            datetime_var=datetime.now(),
            path_var=Path("."),
            set_var={1, 2, 2, 3, 3, 4},
    ):
        self.int_var = int_var
        self.float_var = float_var
        self.str_var = str_var
        self.list_var = list_var
        self.dict_var = dict_var

        self.bytes_var = bytes_var
        self.datetime_var = datetime_var
        self.path_var = path_var
        self.set_var = set_var

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class SampleSubClass(SampleClass):

    def __init__(self, sub_int: int):
        self.sub_int = sub_int


class TestSerialization(unittest.TestCase):

    def test_dump_and_load(self):
        sample = SampleClass(1, float_var=2.5)
        dumped_sample = _serialization.dumps(sample)
        print(dumped_sample)
        loaded_sample = _serialization.loads(dumped_sample)
        self.assertEqual(loaded_sample, sample, f"Dump or load error. Dumped Data:{dumped_sample}")

    def test_dump_and_load_subclass(self):
        sample = SampleSubClass(10)
        dumped_sample = _serialization.dumps(sample)
        print(dumped_sample)
        loaded_sample = _serialization.loads(dumped_sample)
        self.assertEqual(loaded_sample, sample, f"Dump or load error. Dumped Data:{dumped_sample}")

    def test_dump_and_load_unpack_archive(self):
        callback = UnpackArchive(".")
        dumped_callback = _serialization.dumps(callback)
        loaded_callback = _serialization.loads(dumped_callback)
        self.assertEqual(loaded_callback, callback, f"Dump or load error. Dumped Data:{dumped_callback}")
