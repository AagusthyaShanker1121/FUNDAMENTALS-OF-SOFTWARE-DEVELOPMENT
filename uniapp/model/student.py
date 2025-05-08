# from model.person import Person
# from model.enrolment import Enrolment
# from model.course import Course

from random import randint
from person import Person
from enrolment import Enrolment
from course import Course



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

    def enrol(self, student_controller):
        """
        Enrols the student in a course. This method ensures that the student is not enrolled in more than 4 courses.
        It randomly selects a course from the available courses and checks if the student is already enrolled in it.
        If the course is not already enrolled, it creates a new enrolment and adds it to the student's enrolments list.
        """
        courses = Course.load_courses()
        try:
            if len(self.enrolments) == 4:
                raise ValueError("A student can only be enrolled in up to 4 courses.")
            else:
                course_idx = randint(0, len(courses)-1)
                while self.enrolments is None or (courses[course_idx] in [curr_enrol.course for curr_enrol in self.enrolments]):
                    course_idx = randint(0, len(courses)-1)
                new_enrolment = Enrolment(
                    student_id=self.id, 
                    course=courses[course_idx], 
                    semester=randint(1, 2)
                    )
                print(f"New Course: {courses[course_idx]}, Current Courses: {[curr_enrol.course for curr_enrol in self.enrolments]}")
                self.enrolments.append(new_enrolment)
                # student_controller.db.update_enrollment(self.enrollments) 
                return self.enrolments               
        except ValueError as e:
            print(f"Error: {e}")
        except:
            print(f"Error assigning enrolment.")            
    
    def unenrol(self, student_controller):
        if self.enrolments is None or len(self.enrolments) == 0:
            print(f"No subjects enrolled to unenrol from. Enrol first.")
            return None
        rand_idx = randint(0, len(self.enrolments)-1)
        print(f"Course unenrolled: {self.enrolments[rand_idx].course}")
        self.enrolments.pop(rand_idx)
        # student_controller.db.update_enrollment(self.enrollments)
        return self.enrolments

    def get_enrolments(self):
        return self.enrolments
    
    def get_average_mark(self):
        total = sum(e.get_mark() for e in self.enrolments)
        return total / len(self.enrolments)

    def get_grade(self):
        avg = self.get_average_mark()
        if avg >= 85:
            return "HD"
        elif avg >= 75:
            return "D"
        elif avg >= 65:
            return "C"
        elif avg >= 50:
            return "P"
        else:
            return "F"
