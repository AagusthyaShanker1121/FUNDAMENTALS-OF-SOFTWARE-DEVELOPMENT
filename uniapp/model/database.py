from pathlib import Path
import json
from model.student import Student
from model.admin import Admin

class Database:
    db_file_path = Path('data/Students.data')
    
    def __init__(self, db_file_path=db_file_path):
        self.students = {}
        self.admins = {}
        self.load_data()
        self.db_file_path = db_file_path

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
        else:
            file_contents = None
        if file_contents is not None and file_contents != "":
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
    
    def get_data(self):
        return self.load_data()

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

    def delete_data(self, force=False):
        """
        Obliterates the data off the face of this earth.
        After a nice confirmation.
        """
        if force:
            confirmation = None
        else:
            confirmation = input("Are you sure you want to delete all data? (y/n): ")
        
        if confirmation == "y" or force:
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

    def get_student(self, student_id=None, email=None):
        """
        This function checks if there are no students at all as an edge case first.
        Then it will try and find the student by student id first, then email.
        """
        try:
            if self.students in [None, {}]:
                raise ValueError("Cannot get student. No students exist in database.")
            if student_id and student_id in self.students.keys():
                return self.students[student_id]
            elif email:
                for curr_id in self.students.keys():
                    if self.students[curr_id].get_email() == email:
                        return self.students[curr_id]
            else:
                print(f"Student id does not exist: {student_id}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def get_all_students(self):
        return self.students
