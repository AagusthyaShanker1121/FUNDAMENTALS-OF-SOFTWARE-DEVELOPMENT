import pandas as pd
from pathlib import Path
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
        startup_info_path = Path("FOSD")/"uniapp"/"data"/"startup_info.xlsx"
        return list(pd.read_excel(startup_info_path)['Course'])

    def getName(self):
        return self.name
    
    def getUniversity(self):
        return self.university
