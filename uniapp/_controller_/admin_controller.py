from data.database import AdminDb

class AdminController:
    def __init__(self):
        self.db = AdminDb()
        self.logged_in_admin = None
    

    def login(self, username, password) -> bool:
        target_admin = self.db.get_admin()
        if target_admin is None:
            print(f"Admin Not Found or Admin credentials are invalid !")
            return False
        return True
    
    def delete(self, student_id:str, all=False):
        """
        Helper function to delete a particular student or a group of students.
        
        Parameters
        ---
        student_id: str
        all=False: bool
            If set to True deletes entire student data
        """
        # all sets to True so deleting entire data
        if not all:
            if self.db.delete_data(): 
                print("Student Data deleted succesfully.")
            else:
                print("Data cannot be deleted")
            
        else:
            if self.db.delete_student(student_id):
                print("Student deleted successfully.")
            else:
                print("Student doesn't exists.")


    # def add_student(self, student):
    #     self.db.add_student(student)

    def view_all_students(self):
        students = self.db.get_all_students().values()
        print("\nAll Students")
        for student in students:
            print(f"{student.get_name()} :: {student.get_id()} --> Email: {student.get_email()}")

    def view_students_by_grade(self):
        students = self.db.get_all_students().values()
        print("\nGrade Grouping")
        grade_groups = {}
        for student in students:
            grade = student.get_grade()
            entry = f"{student.get_name()} :: {student.get_id()} --> GRADE: {grade} - MARK: {student.get_average_mark():.2f}"
            grade_groups.setdefault(grade, []).append(entry)

        for grade, entries in grade_groups.items():
            print(f"{grade} -->")
            for entry in entries:
                print(f"  {entry}")

    def view_students_by_pass_fail(self):
        students = self.db.get_all_students().values()
        print("\nPASS/FAIL Partition")
        pass_list, fail_list = [], []
        for student in students:
            line = f"{student.get_name()} :: {student.get_id()} --> GRADE: {student.get_grade()} - MARK: {student.get_average_mark():.2f}"
            (pass_list if student.get_average_mark() >= 50 else fail_list).append(line)

        print("FAIL -->")
        for entry in fail_list:
            print(f"  {entry}")
        print("PASS -->")
        for entry in pass_list:
            print(f"  {entry}")
