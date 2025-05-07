import pandas as pd

class Course:
    def __init__(self, name, university):
        self.id = self.generate_id()
        self.name = name
        self.university = university
    
    @staticmethod
    def load_courses():
        """
        Instantiates some courses so we don't need to enter them manually.
        """
        return list(pd.read_excel('data/startup_info.xlsx')['Course'])

    def getName(self):
        return self.name
    
    def getUniversity(self):
        return self.university
