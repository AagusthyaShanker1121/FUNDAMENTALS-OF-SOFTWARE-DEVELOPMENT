import re
import pandas as pd

class Person:
    def __init__(self, name, email, password):
        if not self.validateEmail(email):
            raise ValueError("Invalid email.")
        if not self.validatePassword(password):
            raise ValueError("Invalid password format")
        
        self.name = name
        self.email = email # How do we stop from instantiating this stragight away
        self.password = password

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
        ## TO BE FINISHED
        return True

class Student(Person):
    def __init__(self, name, email, password, id=None): 
        super().__init__(name, email, password) # This retains all original functions in the parents constructor class.
        self.id = id  # Initialize the id attribute
        print(f"Student created! Name: {self.name}, Email: '{self.email}'.")
        # Save data into db file.        

    def set_id(self, id):
        self.id = id
        return self

    @classmethod
    def from_dict(cls, data):
        student = cls(**data)
        return student

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    def enrol(self):
        return "ENROL"
    
    def unenrol(self):
        return "UNENROL"

class Admin(Person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password) # This retains all original functions in the parents constructor class.
        print(f"Student created! Name: {self.name}. Email: {self.email}.")
 
def register_student(db, name, email, password):
    try:
        student = Student(name, email, password)
        student.set_id(db.generate_student_id())
        db.upsert_student(student)
        print(f"Student registered succesfully.")
    except ValueError as e:
        print(f"Error: {e}")        
    return None


def load_admins():
    credentials = pd.read_excel('uniapp/startup_info.xlsx', dtype=str)[['Admin', 'Admin_PW']]
    credentials = credentials.dropna()
    return credentials
