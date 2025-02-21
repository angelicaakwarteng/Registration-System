import pandas as pd
class Register:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def validate_name(name):
        # checking if the name is not empty
        if not name:
            return False, "Name cannot be empty"
        # checking if the name is at least 3 characters long
        if len(name) < 3:
            return False, "Name must be at least 3 characters long"
        # checking if the name is already registered
        if name.count >= 2:
            return False, "Name is already registered"
        
        return True, "Name is valid"
    

    def validate_email(email):
        # checking if the email is not empty
        if not email:
            return False, "Email cannot be empty"
        # checking if the email is valid
        if "@" not in email:
            return False, "Email is not valid"
        # checking if the email is already registered
        if email.count >= 2:
            return False, "Email is already registered"
        
        return True, "Email is valid"
        
    def validate_password(password):
        # checking if the password is not empty
        if not password:
            return False, "Password cannot be empty"
        # checking if the password is at least 8 characters long
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        # checking if the password is valid
        if not password.isalnum():
            return False, "Password must contain both letters and numbers"
        # checking if the password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False, "Password must contain at least one uppercase letter"
        # checking if the password contains at least one lowercase letter
        if not any(char.islower() for char in password):
            return False, "Password must contain at least one lowercase letter"
        # checking if the password contains at least one digit
        if not any(char.isdigit() for char in password):
            return False, "Password must contain at least one digit"
        # checking if the password contains at least one special character
        if not any(char in "!@#$%^&*()_+-=[]{}|;':\",.<>?/" for char in password):
            return False, "Password must contain at least one special character"
        # checking if the password contains at least one space
        if " " in password:
            return False, "Password cannot contain spaces"

        return True
