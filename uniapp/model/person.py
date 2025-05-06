import re

class Person:
    def __init__(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)

    def set_name(self, new_name):
        if new_name and new_name != "":
            self.name = new_name
            return True
        else:
            return False
        
    def set_email(self, new_email):
        if new_email and self.validate_email(new_email):
            self.email = new_email
            return True
        else:
            return False
        
    def set_password(self, new_pw):
        if new_pw and self.validate_password(new_pw):
            self.password = new_pw
            return True
        else:
            return False
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email

    def check_password_match(self, pw_to_check):
        if pw_to_check == self.password:
            return True
        else:
            return False

    @staticmethod
    def validate_email(email):
        email = str(email).lower()
        only_one_at = len(re.findall('@', email)) == 1
        is_suffix = email.endswith('@university.com')
        has_letters_before = len(email.removesuffix('@university.com')) > 0
        ## Also check for special characters !#$%^&*()
        if only_one_at and is_suffix and has_letters_before:
            return True
        else:
            raise ValueError("Invalid email.")
    
    @staticmethod
    def validate_password(password):
        ## TO BE FINISHED
        # raise ValueError("Invalid password format")
        return True