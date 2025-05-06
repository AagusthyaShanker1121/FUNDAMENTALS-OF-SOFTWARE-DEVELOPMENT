import pandas as pd
from model.person import Person

class Admin(Person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password) # This retains all original functions in the parents constructor class.
        print(f"Student created! Name: {self.name}. Email: {self.email}.")

    # logs in to the system
    def login(self) -> bool:
        pass
    
    def delete_course(self, course) -> bool:
        """
        Deletes a course or multiple courses. 

        Parameters
        ---
        course: List[Course] | Course"""
        pass

    def view_course(self, course = 'all') -> None:
        """
        Displays all courses by default.
        For displaying a single or a group of courses, pass in Course or a list[Course]
        
        Parameters
        ---
        course: "all" | Course | List[Course]
        """

        pass

    def delete_student(self, student) -> None:
        """
        Delete a particular student or a group of students that may include the entire class.

        Parameters
        ---
        student: List[Student] | Student
        """
        pass

    def view_students(self, by=None) -> None:
        """
        Displays all enrolled students 
        with or without any conditions.
        Students can be viewed through two conditions- by grade and by pass/fail category.

        Parameters
        ---
        by: Literal ['grade', 'pf']
            if students should be displayed without any condition, then pass 'None'
            if students should be displayed according to grade, then pass 'grade'
            if students should be displayed according to pass/fail category, then pass 'pf' 
        """
        pass

def load_admins():
    credentials = pd.read_excel('uniapp/data/startup_info.xlsx', dtype=str)[['Admin', 'Admin_PW']]
    credentials = credentials.dropna()
    return credentials