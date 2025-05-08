from _controller_.student_controller import StudentController
from _controller_.admin_controller import AdminController
class Menu:

    def __init__(self):

        # Following controllers are responsible for interacting with model and the database
        self.student_controller = None
        self.admin_controller = None
    
    @staticmethod
    def prompt_input(options):
        inpt = input("Enter action to take: " + ''.join(options) + "\n\n")
        return inpt
    
    def inital_menu(self):
        """
        This could also be called the outer menu.
        This is the initial menu which starts on the application.
        And you navigate from here to either the admin or student menu.
        The way I load the options might seem unconventional but I wanted a way to easily
        add and remove options, any additional option added to list will be printed to the user.
        """
        options = [
        "\n\t A: (Admin Menu)",
        "\n\t S: (Student Menu)",
        "\n\t X: (Exit Application)"
        ]
        inpt = self.prompt_input(options)
        while inpt != "X":
            match inpt:
                case "A":
                    # 
                    self.admin_controller = AdminController()
                    self.inital_admin_menu()

                case "S":
                    self.student_controller = StudentController()
                    self.initial_student_menu()
                    pass
                case _:
                    pass
            inpt = self.prompt_input(options)

    def initial_student_menu(self):
        """
        In this function, we have all of the underlying functionality for the student.
        I've managed to get registering down to 3 lines so if we can keep the rest of the
        functionality that succinct I think there will be no need to abstract from here.
        I am using list comprehension which might be hard to interpret to start.
        [input("Enter " + x + ": ") for x in ["name", "email", "password"]] is equivalent to:
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        but the prior creates a list object wiht [name, email, password]
        """
        options = [
        "\n\t l: (student login)",
        "\n\t r: (register)",
        "\n\t c: (change password)",
        "\n\t x: (quit application)"
        ]
        inpt = self.prompt_input(options)
        while inpt != "x":
            match inpt:
                case "l":
                    details = [input("Enter " + x + ": ") for x in ["email", "password"]]
                    if self.student_controller.login(details[0], details[1]):
                        self.student_logged_in_menu()
                case "r":
                    details = [input("Enter " + x + ": ") for x in ["name", "email", "password"]]
                    self.student_controller.register_student(details[0], details[1], details[2])
                case "c":
                    # inpt = input("Enter Student ID or email ID: ")
                    # self.student_controller.change_password(inpt)
                    pass
                case _:
                    pass
            inpt = self.prompt_input(options)
        # If x is entered, log student out.
        self.student_controller.logout()

    def student_logged_in_menu(self):
        curr_student = self.student_controller.logged_in_student
        options = [
        "\n\t e: (enrol in subject)",
        "\n\t u: (unenrol in subject)",
        "\n\t x: (quit application)"
        ]
        inpt = self.prompt_input(options)
        while inpt != "x":
            match inpt:
                case "e":
                    curr_student.enrol(self.student_controller)
                case "u":
                    curr_student.unenrol(self.student_controller)
                case _:
                    pass
            inpt = self.prompt_input(options)



    def intial_admin_menu(self):

        options = [
        "\n\t l: (admin login)"
        ]

        inpt = self.prompt_input(options)
        while inpt != "x":
            match inpt:
                case "l":
                    details = [input("Enter " + x + ": ") for x in ["user name", "password"]]
                    if self.admin_controller.login(details[0], details[1]):
                        self.admin_logged_in_menu()
            inpt = self.prompt_input(options)
        

    def admin_logged_in_menu(self):

        curr_admin = self.admin_controller.logged_in_admin
        options = [
        "\n\t c: (clear entire student database)",
        "\n\t g: (Group students by grade)",
        "\n\t p: (Groups students by pass/fail criteria)",
        "\n\t r: (Remove student)",
        "\n\t s: (Show all students)"
        ]
        inpt = self.prompt_input(options)
        while inpt != "x":
            match inpt:
                case "c":
                    curr_admin.delete(all = True)
                case "g":
                    curr_admin.view_students_by_grade()
                case "p":
                    curr_admin.view_students_by_pass_fail()
                case "r":
                    inpt = input("Enter Student ID: ")
                    curr_admin.delete(inpt)
                case "s":
                    curr_admin.view_all_students()
            inpt = self.prompt_input(options)
