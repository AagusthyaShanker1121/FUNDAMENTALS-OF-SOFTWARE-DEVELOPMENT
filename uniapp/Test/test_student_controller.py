import sys, os, unittest
# ── ① Add the project root (uniapp) to the module search path ──
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from controller.student_controller import StudentController
from model.student import Student

# ── ② Lightweight mock database to simulate real DB behavior ──
class MockDB:
    def __init__(self):
        self.students = {}

    # Implements only the three methods used by StudentController
    def get_student(self, student_id=None, email=None):
        if student_id and student_id in self.students:
            return self.students[student_id]
        if email:
            for stu in self.students.values():
                if stu.get_email() == email:
                    return stu
        return None

    def add_student(self, student):
        self.students[student.get_id()] = student

    def get_all_students(self):
        return self.students

# ── ③ Unit tests ──
class TestStudentControllerLogin(unittest.TestCase):
    def setUp(self):
        """Prepare a clean mock DB and controller before each test."""
        self.db = MockDB()
        self.ctrl = StudentController(self.db)

        # Create and register a test student
        stu = Student("Alice", "alice@university.com", "secret", id="000001")
        stu.set_id("000001")
        self.db.add_student(stu)

    def test_register_and_login(self):
        self.ctrl.register_student("Bob", "bob@university.com", "pass123")
        result = self.ctrl.login("bob@university.com", "pass123")
        self.assertTrue(result)

    def test_login_success(self):
        """Valid credentials → Return True and set session."""
        ok = self.ctrl.login("alice@university.com", "secret")
        self.assertTrue(ok)
        self.assertIsNotNone(self.ctrl.logged_in_student)
        self.assertEqual(self.ctrl.logged_in_student.get_email(), "alice@university.com")

    def test_login_wrong_password(self):
        """Wrong password → Return False and do not keep session."""
        ok = self.ctrl.login("alice@university.com", "wrong")
        self.assertFalse(ok)
        self.assertIsNone(self.ctrl.logged_in_student)

    def test_login_nonexistent_email(self):
        """Nonexistent email → Return False."""
        ok = self.ctrl.login("nobody@university.com", "secret")
        self.assertFalse(ok)
        self.assertIsNone(self.ctrl.logged_in_student)

if __name__ == "__main__":
    unittest.main()
