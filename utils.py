# creating a validate user function to take name, email and password as input
def validate_user(name, email, password):
    # checking if the name is not empty
    if not name:
        return False, "Name cannot be empty"
    # checking if the email is not empty
    if not email:
        return False, "Email cannot be empty"
    # checking if the password is not empty
    if not password:
        return False, "Password cannot be empty"
    # checking if the password is at least 8 characters long
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    # checking if the email is valid
    if "@" not in email:
        return False, "Email is not valid"
    # checking if the email is already registered
    if email in registered_users:
        return False, "Email is already registered"
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
    # checking if the above conditions are met
    else:
        return True, "Welcome! You have successfully registered"
    