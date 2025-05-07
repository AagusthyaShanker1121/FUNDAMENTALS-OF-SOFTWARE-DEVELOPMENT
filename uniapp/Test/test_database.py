import unittest
import sys
from pathlib import Path

# Add the uniapp directory to sys.path
uniapp_root = Path(__file__).resolve().parents[1]
sys.path.append(str(uniapp_root))

from model.student import Student
from model.database import Database

class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        # Capture the initial state
        self._backup_data = self.db.get_all_students()
        print("Data before: {self._backup_data}")

    def tearDown(self):
        # Restore the original data
        self.db.delete_data(force=True)
        for student in self._backup_data.values():
            self.db.add_student(student)

    def test_delete_data(self):
        print(f"Data before: {self.db.get_all_students()}")
        self.db.delete_data(force=True)

        filepath = self.db.db_file_path
        with open(filepath, "r") as f:
            file_content = f.read()
            print(f"File content: {file_content}")

        self.assertEqual(file_content, "")
        self.assertEqual(self.db.get_all_students(), {})
        print(f"Data after: {self.db.get_all_students()}")

if __name__ == "__main__":
    unittest.main()
