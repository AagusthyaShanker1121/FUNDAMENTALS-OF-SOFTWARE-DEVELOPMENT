from users import Student, Admin, register_student, load_admins
from utils import Course, load_courses

def startup():
    courses = load_courses()
    print(f"Courses: {courses}")
    admins = load_admins()
    print(f"Admins: {admins}")
    return courses, admins

def menu():
    def prompt_input():
        options = [
        "\n\t r: (register)",
        "\n\t s: (student login)",
        "\n\t a: (admin login)",
        "\n\t x: (quit application)"
        ]
        inpt = input("Enter action to take: " + ''.join(options) + "\n\n")
        return inpt
    
    inpt = prompt_input()
    while inpt != "x":
        match inpt:
            case "r":
                details = [input("Enter " + x + ": ") for x in ["name", "email", "password"]]
                    # register_student("Sam Williams", "sam@university.com", "password")
                student = register_student(details[0], details[1], details[2])
                # University.add_student(student)
            case "s":
                pass
            case "a":
                pass
            case _:
                pass
        inpt = prompt_input()


def __main__():
    courses, admins = startup()
    menu()

if __name__ == "__main__":
    __main__()
