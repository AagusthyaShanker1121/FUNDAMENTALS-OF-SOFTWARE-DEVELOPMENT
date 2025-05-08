from pathlib import Path
import json
import pandas as pd
# from model.student import Student
# from model.admin import Admin


from model.admin import Admin
from model.student import Student
from model.enrolment import Enrolment

class Database():

    # This class is responsible for the following tasks:
    # 1) retrieving the entire Students.json using load_data() 
    # 2) Saving changes to Students.json using save_data()
    # 3) Retrieving entire startup_info.xlsx file for loading in enrolments

    # Default Path -> AdminDb object may change this path to acess login credentials or course details from startup_info.xlsx file.
    student_db_file_path = Path("FOSD")/"uniapp"/"data"/"Students.json"
    startup_info_file_path = Path("FOSD")/"uniapp"/"data"/"startup_info.xlsx"

    def __init__(self):
        student_data_file = Database.load_data()
        startup_info_file = Database.load_data(Database.startup_info_file_path)

        self._students = {student['id']:student.from_dict()
                          for student in student_data_file['student']
                          }    # Dictionary of all student id and student objects
        
        self._enrollments =  student_data_file['enrolments'] # Dictionary of all student id and their
        
        self._admins = [tuple(row[1:]) for row in startup_info_file[['Admin', 'Admin_PW']].itertuples()]


    # File path defaults to db_file_path if file_path parameters are not passed.  
    def load_data(self, 
                  file_path = None
                  ):
        
        file_contents = None
        if file_path.is_file() and file_path.suffix == '.json':
            with open(file_path, "r") as f:
                file_contents = json.load(f)
        
        if file_path.is_file() and file_path.suffix == '.xlsx':
            file_contents = pd.read_excel(file_path)
        
        return file_contents
    
    def has_student(self, student_id:str = None, student:Student = None) -> bool:

        if student: 
            return (student in self._students.values())
        if student_id:
            return (student_id in self._students.keys())

    def save_data(self) -> bool:
        """
        Saves Student data including any changes made by the admin such as deletion or creation of a single student or multiple students.
        """

        # saving data to Students.json file
        try:
            student_data = [student.from_dict() for student in self.students]
            # enrollment_data = self.enrollments    If in future might need to extract enrollment dictionaries like that in student.

            with open(Database.student_db_file_path, 'r+') as f:
                full_data = json.load(f)
                full_data["students"] = student_data
                full_data["enrolments"] = self.enrollments
                f.seek(0)
                json.dump(full_data, f, indent=4)
                f.truncate()
            return True
        except:
            return False

class AdminDb(Database):

    # This class is responsible for following operations on the retrieved data from Students.json file
    # 1) Deleting a student 
    # 2) Deleting all students  
    # 3) Retreives a particular student using email or student id  
    # 4) Retreives all students 
    # 5) Checks if the admin or student exists or not 

    def __init__(self):
        self.db = Database()

    def get_data(self):
        """
        Returns students and their enrollments
        """
        self.db.load_data()   # Returns all student and enrolment data in Students.json file 

    def has_admin(self, user_name = None, password = None) -> bool:
        return tuple(user_name, password) in self.db._admins
    
    def get_admin(self, username: str, password: str) -> Admin:

        """
        Retrieves the admin by username and password, if it exists, else returns empty tuple
        
        Returns
        ---
        (admin_username, admin_password)
        """
        for admin in self._admins:
            if tuple(username, password) == admin:
                return Admin(username, password)
        
        return None
    
    def delete_data(self, force=False) -> bool:
        """
        Obliterates the data off the face of this earth.
        After a nice confirmation.
        """
        if force:
            confirmation = None
        else:
            confirmation = input("Are you sure you want to delete all data? (y/n): ")
        
        if confirmation == "y" or force:
            # Since save_data() accesses list of students and enrollments, therefore updating the list of students and enrollments with empty dictionary and list.
            self.db._students = {}
            self.db._enrollments = []
            return self.db.save_data()
            
    
    def delete_student(self, student_id: str = None, 
                       student: Student = None) -> bool:
        
        # check if the student exists or not
        if student_id is not None and self.db.has_student(student_id=student_id):
            # delete student 
            self.db._students.pop(student_id)

            # deletes all student enrollment
            for enrolment in self._enrollments:
                if enrolment['student_id'] == student_id:
                    self._enrollments.pop(enrolment)

            self.db.save_data()
            return True
        if student is not None and self.db.has_student(student = student):
            # delete student 
            self.db._students.pop(student['id'])
            # delete student enrollment
            self.db.save_data()
            return True
    
        return False

    
    # This can be used for debugging.
    # def print_data(self):
    #     print(f"Students:  {[student.name for student in self.students.values()]}")
    
    def get_all_students(self) -> dict:
        return self.db._students    # returns a list of students


class StudentDb(Database):

    # This class is responsible for following operations on the retrieved data from Students.data file
    # 1) creating a student (basically the student registers itself)
    # 2) updates 
    # 5) Retrieves a particular student record.

    def __init__(self):
        self.db = Database()

    def add_student(self, student:Student) -> None:
        """
        Inserts a unique student record in the database.

        Parameters
        ---
        student: Student
        """
        if student:
            # Add new a student if it doesn't exists.
            if self.db.has_student() is False:
                # append to the students list
                self.db._students[student['id']] = student
                print(f"Student {student.name} inserted succesfully.")
                self.save_data()
            
            else:
                print(f"Student {student.name} already exists.")
    

    
    def get_student(self, student_id=None, email=None) -> Student:
        """
        This function checks if there are no students at all as an edge case first.
        Then it will try and find the student by student id first, then email.
        """
        try:
            if self.db._students is None or self.db._students == {}:
                raise ValueError("Cannot get student. No students exist in database.")
            if student_id and (student_id in self.db._students.keys()):
                return self.db._students[student_id]    # returns a student object
            elif email:
                for curr_id in self.db._students.keys():
                    if self.db._students[curr_id].get_email() == email:   # get_email() is not present in Student
                        return self.db._students[curr_id]
                else:
                    print(f"Student id does not exist: {student_id}")
                    return None
        except ValueError as e:
            print(f"Error: {e}")
    

    def update_password(self, student_id, new_password) -> False:

        """
        - changes the password of the student
        """
        if self.db.has_student(student_id) is False:
            return False

        self.db._students['student_id']['password'] = new_password
        self.db.save_data()
        return True
    
    # def update_enrollment(self, enrollment):
    #     self.db._enrollments = enrollment
    #     self.db.save_data()




