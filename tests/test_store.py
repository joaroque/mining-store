"""Integration tests for the educational CSV sales program."""

import csv
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.directory = Path(self.temporary_directory.name) / "mining_store"
        shutil.copytree(
            PROJECT_DIR,
            self.directory,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "tests"),
        )

    def run_program(self, user_input):
        return subprocess.run(
            [sys.executable, "main.py"],
            cwd=self.directory,
            input=user_input,
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=True,
        ).stdout

    def read_data(self, file_name):
        with (self.directory / "data" / file_name).open(
            encoding="utf-8-sig", newline=""
        ) as file:
            return list(csv.DictReader(file, delimiter=";"))

    def test_sale_is_saved_and_persists_after_restart(self):
        output = self.run_program("2\n1\n2\n3\n4\n0\n")
        self.assertIn("Сумма продажи: 3000 руб.", output)
        self.assertIn("Общая сумма продаж: 3000 руб.", output)
        self.assertEqual("8", self.read_data("products.csv")[0]["quantity"])
        self.assertEqual("3000", self.read_data("sales.csv")[0]["total"])

        output_after_restart = self.run_program("1\n3\n0\n")
        self.assertIn("На складе: 8 шт.", output_after_restart)
        self.assertIn("Общая сумма продаж: 3000 руб.", output_after_restart)

    def test_invalid_sales_do_not_change_files(self):
        output = self.run_program("2\n1\n0\n2\n1\n99\n2\n999\n1\n0\n")
        self.assertIn("Ошибка:", output)
        self.assertEqual("10", self.read_data("products.csv")[0]["quantity"])
        self.assertEqual([], self.read_data("sales.csv"))


if __name__ == "__main__":
    unittest.main()
