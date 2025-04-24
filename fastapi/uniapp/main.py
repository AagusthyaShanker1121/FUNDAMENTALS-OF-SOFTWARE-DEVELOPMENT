from uniapp.users import load_admins
from uniapp.utils import Menu, load_courses
from uniapp.database import Database

def startup():
    courses = load_courses()
    admins = load_admins()
    return courses, admins

def initialize_app():
    courses, admins = startup()
    db = Database()
    menu = Menu(db)
    return {
        "courses": courses,
        "admins": admins,
        "db": db,
        "menu": menu,
    }

def __main__():
    app_objects = initialize_app()
    app_objects["menu"].run_menu()

if __name__ == "__main__":
    __main__()