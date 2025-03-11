from register_view import register_user
from  register_model import validate_name, validate_email, validate_password
import pytest

def register_user(name, email, password):
    name_valid, name_error = validate_name(name)
    email_valid, email_error = validate_email(email)
    password_valid, password_error = validate_password(password)
    if name_valid and email_valid and password_valid:
        return True, "User registered successfully"
    else:
        # returning the error messages
        return False, name_error + email_error + password_error


def test_register_user():
  assert register_user('Angelica', 'angiekwart32@gmail.com', '*****')
