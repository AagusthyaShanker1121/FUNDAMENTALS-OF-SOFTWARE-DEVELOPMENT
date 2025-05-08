import pandas as pd
# from model.person import Person
# from FOSD.uniapp.model.user.person import Person
from user.person import Person
from pathlib import Path

class Admin(Person):
    def __init__(self, username:str, password:str):
        super().__init__(username, password) # This retains all original functions in the parents constructor class.

    
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

    def delete_individual_student(self, student_id: str) -> None:
        inpt = input("Enter the student ID: ")
        self.db.load_data()
        
        for student in self.students:
            if inpt == student["id"]:
                self.students.remove(student)
                self.save_data()
                print(f"Student {student_id} deleted successfully.")
                return
        
        print(f"Student {inpt} not found.")
        
    def clear_all_students(self) -> None:
        confirmation = input("Are you sure you want to delete all data? (y/n): ")
        if confirmation == "y":
            with open(self.db_file_path, "w") as f:
                f.write("")
            self.load_data()
            print("Data deleted successfully.")
        
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

# def load_admins():
#     startup_info_path = Path("FOSD")/"uniapp"/"data"/"startup_info.xlsx"
#     credentials = pd.read_excel(startup_info_path, dtype=str)[['Admin', 'Admin_PW']]
#     credentials = credentials.dropna()
#     return credentials