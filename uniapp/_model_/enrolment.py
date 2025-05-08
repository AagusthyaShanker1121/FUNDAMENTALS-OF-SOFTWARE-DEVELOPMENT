from random import randint
from database import AdminDb

class Enrolment():
    def __init__(self, student_id, course, semester, enrolment_id=None):
        self.assign_id()
        self.student_id = student_id
        self.course = course
        self.assign_mark()
        self.grade = self.generate_grade()
        pass

    def assign_id(self):
        """
        This retrieves all enrolment ids to ensure a unique id by cycling
        two nested loops, for each student, grab each enrolment id.
        """
        all_students = AdminDb().get_all_students()
        all_enrolment_ids = []
        for curr_student in all_students.values():
            if len(curr_student.get_enrolments()) > 0:
                for curr_enrolment in curr_student.get_enrolments():
                    all_enrolment_ids.append(curr_enrolment.get_id())
        # Now assign an id not in all_enrolment_ids.
        new_id = str(randint(1, 400000))
        while new_id in all_enrolment_ids:
            new_id = str(randint(1, 400000))
        # Pad the new id out to 6 characters ie; 000001
        while len(new_id) < 6:
            new_id = "0" + new_id
        self.enrolment_id = new_id

    def assign_mark(self):
        self.mark = randint(0, 100)
    
    def generate_grade(self):
        m = self.mark
        if m is None:
            raise ValueError("Error: Mark does not exist.")
        if m >= 85:
            return "HD"
        elif m >= 75:
            return "D"
        elif m >= 65:
            return "C"
        elif m >= 50:
            return "P"
        else:
            return "F"

    def get_id(self):
        return self.enrolment_id


