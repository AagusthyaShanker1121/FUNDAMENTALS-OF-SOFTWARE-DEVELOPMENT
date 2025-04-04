from users import Student, Admin, register_student
from utils import Course, load_courses


def __main__():
    sam = register_student("Sam Williams", "sam@university.com@@", "password")

if __name__ == "__main__":
    __main__()
