import pandas as pd
from pathlib import Path
from users import Student, register_student
import json

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
    db_file_path = Path('bankapp/Students.data')
    
    def __init__(self):
        if self.db_file_path.is_file():
            print('DB exists!')
        else:
            print('DB does not exist.')
        pass



class Menu:
    @staticmethod
    def prompt_input():
        options = [
        "\n\t r: (register)",
        "\n\t s: (student login)",
        "\n\t a: (admin login)",
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
                    student = register_student(details[0], details[1], details[2])
                    # University.add_student(student)
                case "s":
                    pass
                case "a":
                    pass
                case _:
                    pass
            inpt = self.prompt_input()


def load_courses():
    return list(pd.read_excel('uniapp/startup_info.xlsx')['Course'])
  