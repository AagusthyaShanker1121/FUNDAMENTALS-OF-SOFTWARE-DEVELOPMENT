from users import load_admins
from utils import Menu, load_courses
from database import Database

def startup():
    courses = load_courses()
    # print(f"Courses: {courses}")
    admins = load_admins()
    # print(f"Admins: {admins}")
    return courses, admins


def __main__():
    courses, admins = startup()
    db = Database()
    menu = Menu(db)
    menu.run_menu()

if __name__ == "__main__":
    __main__()
