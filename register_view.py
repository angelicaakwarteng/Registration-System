# parameters to use for the registration system
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
registered_users = {
        "name": name,
        "email": email,
        "password": password
    }

def validate_name(name):
    # checking if the name is not empty
    if not name:
        return False, "Name cannot be empty"
    # checking if the name is at least 3 characters long
    if len(name) < 3:
        return False, "Name must be at least 3 characters long"
    # checking if the name is same as the email
    if name == email:
        return True
    

def validate_email(email):
    # checking if the email is not empty
    if not email:
        return False, "Email cannot be empty"
    # checking if the email is valid
    if "@" not in email:
        return False, "Email is not valid"
    # checking if the email is already registered
    if email in registered_users:
        return False, "Email is already registered"
    
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
    

# creating a function to register user which takes name, email and password as input
def register_user(name, email, password):
    # calling the validate_name function to check if the name is valid
    name_valid, name_error = validate_name(name)
    # calling the validate_email function to check if the email is valid
    email_valid, email_error = validate_email(email)
    # calling the validate_password function to check if the password is valid
    password_valid, password_error = validate_password(password)
    # checking if the name, email and password are valid
    if name_valid and email_valid and password_valid:
        # adding the user to the registered_users list
        return True, "User registered successfully"
    else:
        # returning the error messages
        return False, name_error + email_error + password_error