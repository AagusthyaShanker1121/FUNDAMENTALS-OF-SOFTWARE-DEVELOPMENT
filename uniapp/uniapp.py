import pandas as pd
from pathlib import Path
import re
# Database
# Student
# Enrolment

# Read in courses

class Person:
    def __init__(self, name, email, password):
        if not self.validateEmail(email):
            raise ValueError("Invalid email.")
        if not self.validatePassword(password):
            raise ValueError("Invalid password format")
        
        self.id = self.generate_id()
        self.name = name
        self.email = email # How do we stop from instantiating this stragight away
        self.password = password

    def generate_id():
        return "Id"
    
    def setName(self, new_name):
        if new_name:
            self.name = new_name
            return True
        else:
            return False
        
    def setEmail(self, new_email):
        if new_email and self.validateEmail(new_email):
            self.email = new_email
            return True
        else:
            return False
        
    def setPassword(self, new_pw):
        if new_pw and self.validatePassword(new_pw):
            self.password = new_pw
            return True
        else:
            return False
    
    @staticmethod
    def validateEmail(email):
        email = str(email).lower()
        only_one_at = re.findall('@', email)
        only_one_at = len(only_one_at) == 1
        is_suffix = email.endswith('@university.com')
        ## Also check for special characters !#$%^&*()
        if only_one_at and is_suffix:
            return True
        else:
            return False
    
    @staticmethod
    def validatePassword(password):
        return None
        ## TO BE FINISHED

class Student(Person):
    # def __init__(super, self):
    #     print(f"Student created: {self.name}")

    def enrol(self):
        return "ENROL"
    

class Course:
    def __init__(self, name, university):
        self.id = self.generate_id()
        self.name = name
        self.university = university
    
    def getName(self):
        return self.name
    
    def getUniversity(self):
        return self.university

class Admin:
    def __init__(self):
        self.admins = pd.read_excel('bankapp/startup_info.xlsx', dtype=str)['Admin']
        self.admins = list(self.admins[self.admins.notna()])
        self.admin_pws = pd.read_excel('bankapp/startup_info.xlsx', dtype=str)['Admin_PW']
        self.admin_pws = list(self.admin_pws[self.admin_pws.notna()])
    
class Database:
    db_file_path = Path('bankapp/Students.data')
    
    def __init__(self):
        if self.db_file_path.is_file():
            print('DB exists!')
        else:
            print('DB does not exist.')
    
    def register_student(self, name, email, password):
        details_match_criteria = Student.validate_email(email) & Student.validate_pw(password)
        if details_match_criteria:
            return Student(name, email, password)
        else:
            return "Show error message"


def __main__():
    # courses = list(pd.read_excel('bankapp/startup_info.xlsx')['Course'])
    try:
        student = Student("Sam Williams", "sam@university.com", "password")
        print(student.name)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    __main__()
