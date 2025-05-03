from pathlib import Path
import json
import random
from users import Student, Admin

class Database:
    db_file_path = Path('uniapp/Students.data')
    
    def __init__(self):
        self.students = {}
        self.admins = {}
        self.load_data()

    def load_data(self):
        """
        This function checks if the students.data file exists first
        Then if it does and is not empty, it will load the data into json format (dictionary).
        This data is then stored in self.data.
        self.data is used elsewhere to store local variables 
        such as self.students and self.admins
        """
        if self.db_file_path.is_file():
            with open(self.db_file_path, "r") as f:
                file_contents = f.read()
        if file_contents and file_contents != "":
            self.data = json.loads(file_contents)
            print(file_contents)
        else:
            self.data = {
            'students': None,
            'admins': None
            }
        if self.data['students'] is not None:
            for student in self.data.get('students', []):
                self.students[student['id']] = Student.from_dict(student)
        else:
            # This is required otherwise the students object does not reset after deleting data.
            self.students = {}
        # self.load_admins()
        # Admin load needs to be completed.
        # for admin in self.data.get('admins', []):
        #     self.admins = [Admin.from_dict(admin)] 

    def save_data(self):
        """
        Creates a dictionary with only two keys ("students" & "admins")
        Inside each key, the students and admin objects are converted from their
        Object format into a dictionary. So they can easily be reinstated.
        """
        self.data = {
            "students": [self.students[curr_student].to_dict() for curr_student in self.students]
            # "admins": 
        }
        with open(self.db_file_path, "w") as f:
            f.write(json.dumps(self.data))
            f.close()
        print("Data saved succesfully.")
        return None

    def delete_data(self):
        """
        Obliterates the data off the face of this earth.
        After a nice confirmation.
        """
        confirmation = input("Are you sure you want to delete all data? (y/n): ")
        if confirmation == "y":
            with open(self.db_file_path, "w") as f:
                f.write("")
                f.close()
            self.load_data()
            print("Data deleted succesfully.")

    def add_student(self, student):
        """
        The term 'upsert' is used here, because what this function does is:
        If the student exists in the database, it replaces the existing data.
        If it does not exist, it creates it for the first time.
        """
        if student:
            self.students[student.id] = student
            print(f"Student {student.name} upserted succesfully.")
            self.save_data()
    
    def print_data(self):
        print(f"Students:  {[student.name for student in self.students.values()]}")

class StudentController:
    def __init__(self, db):
        self.db = db

    def register_student(self, name, email, password):
        try:
            self.validate_unique_email(email)
            student = Student(name, email, password)
            student.set_id(self.generate_student_id())
            self.db.add_student(student)
            print(f"Student registered successfully.")
        except ValueError as e:
            print(f"Error: {e}")        
        return None
    
    def validate_unique_email(self, email):
        # Validate email does not exist.
        all_students = self.get_all_students()
        if email in [student.get_email() for student in all_students.values()]:
            raise ValueError("Email already exists.")

    def generate_student_id(self):
        """
        This function works well as an instance method since it uses the database.
        """
        id = random.randint(1, int(1e6 - 1))
        while id in self.db.students.keys():
            # Generate a new int if id already exists
            id = random.randint(1, int(1e6 - 1))
        id = str(id)
        while len(id) < 6:
            id = "0" + id
        return id
    
    def get_student(self, student_id):
        if student_id in self.db.students.keys():
            return self.db.students[student_id]
        else:
            print(f"Student id does not exist: {student_id}")
    
    def get_all_students(self):
        return self.db.students

