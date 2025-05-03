import pandas as pd
from pathlib import Path
from users import Student
from db_utils import StudentController

class Course:
    def __init__(self, name, university):
        self.id = self.generate_id()
        self.name = name
        self.university = university
    
    @staticmethod
    def load_courses():
        """
        Instantiates some courses so we don't need to enter them manually.
        """
        return list(pd.read_excel('uniapp/startup_info.xlsx')['Course'])

    def getName(self):
        return self.name
    
    def getUniversity(self):
        return self.university

class Enrolment:
    def __init__(self, student, course, semester, student_controller):
        self.assign_id(student_controller)
        self.generate_mark()
        self.generate_grade()
        pass

    def assign_id(self, student_controller):
        """
        How do we ensure a unique id?
        We need to access the db to return all current enrolment ids.
        This retrieves all enrolment ids by cycling
        Two nested loops, for each student, grab each enrolment id.
        """
        all_students = student_controller.get_all_students()
        all_enrolment_ids = []
        for curr_student in all_students.values():
            if len(curr_student.get_enrolments()) > 0:
                for curr_enrolment in curr_student.get_enrolments():
                    all_enrolment_ids.append(curr_enrolment.get_id())
        # Now assign an id not in all_enrolment_ids.

    def generate_mark(self):
        """
        
        """
        self.mark = ""
        return None
    
    def generate_grade(self):
        self.grade = ""
        pass

    def get_id(self):
        return self.id

    def get_mark(self):
        return self.mark
    
    def get_grade(self):
        return self.grade

class Menu:
    def __init__(self, db):
        """
        The db object is required in the menu class because
        There needs to be an intermediary object between the users input
        and the database. This is the menu class atm but we could change it.
        """
        self.db = db
        self.student_controller = StudentController(self.db)

        return None
    
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
                    # admin_menu()
                    pass
                case "S":
                    self.student_menu()
                    pass
                case _:
                    pass
            inpt = self.prompt_input(options)

    def student_menu(self):
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
        "\n\t r: (register)",
        "\n\t s: (student login)",
        "\n\t a: (admin login)",
        "\n\t p: (show data in database)",
        "\n\t d: (delete data in database)",
        "\n\t x: (quit application)"
        ]
        inpt = self.prompt_input(options)
        while inpt != "x":
            match inpt:
                case "r":
                    details = [input("Enter " + x + ": ") for x in ["name", "email", "password"]]
                    self.student_controller.register_student(details[0], details[1], details[2])
                case "s":
                    pass
                case "a":
                    pass
                case "p":
                    # We can delete this after, just for debugging.
                    self.db.print_data()
                case "d":
                    self.db.delete_data()
                case _:
                    pass
            inpt = self.prompt_input(options)
