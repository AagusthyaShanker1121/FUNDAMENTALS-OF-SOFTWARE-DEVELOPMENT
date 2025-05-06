from model.person import Person
from model.enrolment import Enrolment
from random import randint

class Student(Person):
    def __init__(self, name, email, password, id=None, enrolments=None): 
        super().__init__(name, email, password) # This retains all original functions in the parents constructor class.
        self.id = id  
        if enrolments is not None:
            self.enrolments = enrolments
        else:
            self.enrolments = []
        print(f"Student created! Name: {self.name}, Email: '{self.email}'.")        

    def set_id(self, id):
        self.id = id
        return self

    @classmethod
    def from_dict(cls, data):
        student = cls(**data)
        return student

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    def enrol(self, courses, student_controller):
        """
        Enrols the student in a course. This method ensures that the student is not enrolled in more than 4 courses.
        It randomly selects a course from the available courses and checks if the student is already enrolled in it.
        If the course is not already enrolled, it creates a new enrolment and adds it to the student's enrolments list.
        """
        try:
            if len(self.enrolments) == 4:
                raise ValueError("A student can only be enrolled in up to 4 courses.")
            else:
                while self.enrolments is None or courses[course_idx] in [curr_enrol.course for curr_enrol in self.enrolments]:
                    print(f"New Course: {courses[course_idx]}, Current Courses: {[curr_enrol.course for curr_enrol in self.enrolments]}")
                    course_idx = randint(0, len(courses))
                new_enrolment = Enrolment(
                    student=self, 
                    course=courses[course_idx], 
                    semester=randint(1, 2), 
                    student_controller=student_controller)
                self.enrolments.append(new_enrolment)
        except:
            print(f"Error assigning enrolment.")            
    
    def unenrol(self):
        return "UNENROL"

    def get_enrolments(self):
        return self.enrolments
