import re
import pandas as pd
from random import randint
from utils import Enrolment

class Person:
    def __init__(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)

    def set_name(self, new_name):
        if new_name and new_name != "":
            self.name = new_name
            return True
        else:
            return False
        
    def set_email(self, new_email):
        if new_email and self.validate_email(new_email):
            self.email = new_email
            return True
        else:
            return False
        
    def set_password(self, new_pw):
        if new_pw and self.validate_password(new_pw):
            self.password = new_pw
            return True
        else:
            return False
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email

    def check_password_match(self, pw_to_check):
        if pw_to_check == self.password:
            return True
        else:
            return False

    @staticmethod
    def validate_email(email):
        email = str(email).lower()
        only_one_at = len(re.findall('@', email)) == 1
        is_suffix = email.endswith('@university.com')
        has_letters_before = len(email.removesuffix('@university.com')) > 0
        ## Also check for special characters !#$%^&*()
        if only_one_at and is_suffix and has_letters_before:
            return True
        else:
            raise ValueError("Invalid email.")
    
    @staticmethod
    def validate_password(password):
        ## TO BE FINISHED
        # raise ValueError("Invalid password format")
        return True

class Student(Person):
    def __init__(self, name, email, password, id=None, enrolments=None): 
        super().__init__(name, email, password) # This retains all original functions in the parents constructor class.
        self.id = id  
        if enrolments is not None:
            self.enrolments = enrolments
        else:
            self.enrolments = []
        print(f"Student created! Name: {self.name}, Email: '{self.email}'.")        

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

    def enrol(self, courses, student_controller):
        """
        Enrols the student in a course. This method ensures that the student is not enrolled in more than 4 courses.
        It randomly selects a course from the available courses and checks if the student is already enrolled in it.
        If the course is not already enrolled, it creates a new enrolment and adds it to the student's enrolments list.
        """
        try:
            if len(self.enrolments) == 4:
                raise ValueError("A student can only be enrolled in up to 4 courses.")
            else:
                while self.enrolments is None or courses[course_idx] in [curr_enrol.course for curr_enrol in self.enrolments]:
                    print(f"New Course: {courses[course_idx]}, Current Courses: {[curr_enrol.course for curr_enrol in self.enrolments]}")
                    course_idx = randint(0, len(courses))
                new_enrolment = Enrolment(
                    student=self, 
                    course=courses[course_idx], 
                    semester=randint(1, 2), 
                    student_controller=student_controller)
                self.enrolments.append(new_enrolment)
        except:
            print(f"Error assigning enrolment.")            
    
    def unenrol(self):
        return "UNENROL"

    def get_enrolments(self):
        return self.enrolments

class Admin(Person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password) # This retains all original functions in the parents constructor class.
        print(f"Student created! Name: {self.name}. Email: {self.email}.")

def load_admins():
    credentials = pd.read_excel('uniapp/startup_info.xlsx', dtype=str)[['Admin', 'Admin_PW']]
    credentials = credentials.dropna()
    return credentials
