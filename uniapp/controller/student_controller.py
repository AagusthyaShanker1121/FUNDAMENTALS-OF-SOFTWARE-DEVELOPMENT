import random
from model.student import Student

class StudentController:
    def __init__(self, db):
        self.db = db
        self.logged_in_student = None

    def login(self, email, password):
        target_student = self.db.get_student(email=email)
        if target_student is not None:
            if target_student.check_password_match(password):
                self.logged_in_student = target_student
                print(f"Student Log In Succesful: Student: {target_student.get_name()}, Email: {target_student.get_email()}")
            else:
                raise ValueError("Password does not match.")
        else:
            raise ValueError("Email does not exist.")

    def logout(self):
        self.logged_in_student = None
    
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
        all_students = self.db.get_all_students()
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
    
