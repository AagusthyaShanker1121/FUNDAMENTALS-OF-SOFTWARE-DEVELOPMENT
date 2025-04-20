import re
import pandas as pd

class Person:
    def __init__(self, name, email, password):
        if not self.validateEmail(email):
            raise ValueError("Invalid email.")
        if not self.validatePassword(password):
            raise ValueError("Invalid password format")
        
        self.id = Person.generate_id()
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
        return True
        ## TO BE FINISHED

class Student(Person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password) # This retains all original functions in the parents constructor class.
        print(f"Student created! Name: {self.name}. Email: {self.email}.")
        # Save data into db file.

    def enrol(self):
        return "ENROL"
    
class Admin(Person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password) # This retains all original functions in the parents constructor class.
        print(f"Student created! Name: {self.name}. Email: {self.email}.")
 
def register_student(name, email, password):
    try:
        return Student(name, email, password)
    except ValueError as e:
        print(f"Error: {e}")

def load_admins():
    credentials = pd.read_excel('uniapp/startup_info.xlsx', dtype=str)[['Admin', 'Admin_PW']]
    credentials = credentials.dropna()
    return credentials
