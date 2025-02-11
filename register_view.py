from  register_model import validate_name, validate_email, validate_password

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
