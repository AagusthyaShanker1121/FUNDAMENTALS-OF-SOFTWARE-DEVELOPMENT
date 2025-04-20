from users import Student, Admin, register_student, load_admins
from utils import Course, Menu, load_courses

def startup():
    courses = load_courses()
    print(f"Courses: {courses}")
    admins = load_admins()
    print(f"Admins: {admins}")
    return courses, admins


def __main__():
    courses, admins = startup()
    menu = Menu()
    menu.run_menu()

if __name__ == "__main__":
    __main__()
