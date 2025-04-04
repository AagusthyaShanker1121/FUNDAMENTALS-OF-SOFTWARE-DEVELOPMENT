import pandas as pd
from pathlib import Path

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
    
    def register_student(self, name, email, password):
        details_match_criteria = Student.validate_email(email) & Student.validate_pw(password)
        if details_match_criteria:
            return Student(name, email, password)
        else:
            return "Show error message"


def load_courses():
    return list(pd.read_excel('bankapp/startup_info.xlsx')['Course'])
  