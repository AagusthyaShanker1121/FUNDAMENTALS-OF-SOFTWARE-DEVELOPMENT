import pandas as pd
from person import Person
from pathlib import Path

class Admin(Person):
    def __init__(self, username:str, password:str):
        super().__init__(username, password) # This retains all original functions in the parents constructor class.
