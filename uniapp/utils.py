import pandas as pd
from pathlib import Path
from users import Student, Admin, register_student
import json
import random

class Course:
    def __init__(self, name, university):
        self.id = self.generate_id()
        self.name = name
        self.university = university
    
    def getName(self):
        return self.name
    
    def getUniversity(self):
        return self.university

class Database:
    db_file_path = Path('uniapp/Students.data')
    
    def __init__(self):
        self.students = {}
        self.admins = {}
        self.load_data()

    def load_data(self):
        if self.db_file_path.is_file():
            print("DB Exists!")
            with open(self.db_file_path, "r") as f:
                self.data = json.loads(f.read())  # Read file content before parsing
        else:
            print('DB does not exist.')
            self.data = {
                'Students': None,
                'Admins': None
            }
        for student in self.data.get('students', []):
            self.students[student['id']] = Student.from_dict(student)
        # for admin in self.data.get('admins', []):
        #     self.admins = [Admin.from_dict(admin)] 
        print(self.data)
    
    def save_data(self):
        self.data = {
            "students": [self.students[curr_student].to_dict() for curr_student in self.students]
            # "admins": 
        }
        with open(self.db_file_path, "w") as f:
            f.write(json.dumps(self.data))
            f.close()
        print("Data saved succesfully.")
        return None

    def generate_student_id(self):
        """
        This function exists on the database class because it requires 
        access to all of the existing ids in the database. 
        If this function existed on the student class it would require 
        the student class to have access to the database while instantiating 
        which would be messy.
        """
        id = random.randint(1, int(1e6 - 1))
        while id in self.students.keys():
            # Generate a new int if id already exists
            id = random.randint(1, int(1e6 - 1))
        return id

    def upsert_student(self, student):
        if student:
            self.students[student.id] = student
            print(f"Student {student.name} upserted succesfully.")
            self.save_data()
    
    def print_data(self):
        print(f"Students:  {[student.name for student in self.students.values()]}")

class Menu:
    def __init__(self, db):
        self.db = db
        return None
    
    @staticmethod
    def prompt_input():
        options = [
        "\n\t r: (register)",
        "\n\t s: (student login)",
        "\n\t a: (admin login)",
        "\n\t p: (show data in database)",
        "\n\t x: (quit application)"
        ]
        inpt = input("Enter action to take: " + ''.join(options) + "\n\n")
        return inpt
    
    def run_menu(self):
        inpt = self.prompt_input()
        while inpt != "x":
            match inpt:
                case "r":
                    details = [input("Enter " + x + ": ") for x in ["name", "email", "password"]]
                    student = register_student(self.db, details[0], details[1], details[2])
                    self.db.upsert_student(student)
                case "s":
                    pass
                case "a":
                    pass
                case "p":
                    self.db.print_data()
                case _:
                    pass
            inpt = self.prompt_input()

def load_courses():
    return list(pd.read_excel('uniapp/startup_info.xlsx')['Course'])
