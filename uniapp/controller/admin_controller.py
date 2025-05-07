class AdminController:
    def __init__(self, db):
        self.db = db

    def add_student(self, student):
        self.db.add_student(student)

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
