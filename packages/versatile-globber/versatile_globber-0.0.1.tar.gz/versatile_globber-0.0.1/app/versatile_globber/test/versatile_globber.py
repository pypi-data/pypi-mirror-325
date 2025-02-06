import os
import shutil
import unittest

from pathlib import Path

from app.versatile_globber.src.versatile_globber import versatile_glob

from app.versatile_globber.test.test_utils import create_file

class TestVersatileGlobber(unittest.TestCase):
    def setUp(self):
        self.expected_filepaths = [
            r"temp\abc_1.txt",
            r"temp\abc_2.txt",
            r"temp\abc_3.txt",
            r"temp\temp.py",
            r"another_temp\temp.py"
        ]

        for item in self.expected_filepaths:
            create_file(item)

    def test_only_folders(self):
        extensions = [".txt", ".py"]
        path = [
            r"temp",
            r"another_temp\temp.py"
        ]

        filepaths = versatile_glob(path, extensions)

        self.assertCountEqual(self.expected_filepaths, filepaths)

    def tearDown(self):
        for i in self.expected_filepaths:
            if os.path.exists(i):
                shutil.rmtree(Path(i).parts[0])