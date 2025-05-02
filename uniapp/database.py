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
                # Initialize self.data with all current data
                # Inside the students.data file.
                if file_contents and file_contents != "":
                    self.data = json.loads(file_contents)
                else:
                    self.data = {
                    'students': None,
                    'admins': None
                }
        if self.data['students'] is not None:
            for student in self.data.get('students', []):
                self.students[student['id']] = Student.from_dict(student)
        else:
            self.students = {}
        # Admin load needs to be completed.
        # for admin in self.data.get('admins', []):
        #     self.admins = [Admin.from_dict(admin)] 
        print(self.data)
    
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

    def generate_student_id(self):
        """
        This function exists on the database class because it requires 
        access to all of the existing ids in the database. 
        If this function existed on the student class it would require 
        the student class to have access to the database while instantiating 
        which would be messy. 
        This is where StudentController would make sense to use.
        """
        id = random.randint(1, int(1e6 - 1))
        while id in self.students.keys():
            # Generate a new int if id already exists
            id = random.randint(1, int(1e6 - 1))
        id = str(id)
        while len(id) < 6:
            id = "0" + id
        return id

    def upsert_student(self, student):
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
