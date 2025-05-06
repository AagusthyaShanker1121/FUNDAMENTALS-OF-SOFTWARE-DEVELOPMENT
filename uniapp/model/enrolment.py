from random import randint

class Enrolment:
    def __init__(self, student, course, semester, student_controller):
        self.assign_id(student_controller)
        self.generate_mark()
        self.generate_grade()
        pass

    def assign_id(self, student_controller):
        """
        This retrieves all enrolment ids to ensure a unique id by cycling
        two nested loops, for each student, grab each enrolment id.
        """
        all_students = student_controller.get_all_students()
        all_enrolment_ids = []
        for curr_student in all_students.values():
            if len(curr_student.get_enrolments()) > 0:
                for curr_enrolment in curr_student.get_enrolments():
                    all_enrolment_ids.append(curr_enrolment.get_id())
        # Now assign an id not in all_enrolment_ids.
        while new_id is None or new_id in all_enrolment_ids:
            new_id = randint(1, 400000)
        # Pad the new id out to 6 characters ie; 000001
        while len(new_id) < 6:
            new_id = "0" + new_id
        return new_id

    def generate_mark(self):
        """
        
        """
        self.mark = ""
        return None
    
    def generate_grade(self):
        self.grade = ""
        pass

    def get_id(self):
        return self.id

    def get_mark(self):
        return self.mark
    
    def get_grade(self):
        return self.grade
