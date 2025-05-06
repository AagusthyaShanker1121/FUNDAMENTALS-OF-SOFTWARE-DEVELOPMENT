class AdminController:
    def add_student(self, student):
        self.db.add_student(student)