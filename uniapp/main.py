from users import load_admins
from utils import Menu, Course
from database import Database

def startup():
    courses = Course.load_courses()
    admins = load_admins()
    return courses, admins

def __main__():
    # This info is used to instantiate courses and admins for debugging
    # So we don't have to create them everytime you load the app.
    courses, admins = startup()

    # Main Script
    db = Database()
    menu = Menu(db)
    menu.inital_menu()

if __name__ == "__main__":
    __main__()
