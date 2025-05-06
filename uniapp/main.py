from model.admin import load_admins
from model.course import Course
from model.database import Database
from view.menu import Menu

def __main__():
    # This info is used to instantiate courses and admins for debugging
    # So we don't have to create them everytime you load the app.
    courses = Course.load_courses()
    admins = load_admins()

    # Main Script
    db = Database()
    menu = Menu(db)
    menu.inital_menu()

if __name__ == "__main__":
    __main__()
