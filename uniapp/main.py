from users import Student, Admin, register_student, load_admins
from utils import Course, load_courses

def startup():
    courses = load_courses()
    print(f"Courses: {courses}")
    admins = load_admins()
    print(f"Admins: {admins}")
    return courses, admins

def __main__():
    sam = register_student("Sam Williams", "sam@university.com", "password")
    courses, admins = startup()

if __name__ == "__main__":
    __main__()
