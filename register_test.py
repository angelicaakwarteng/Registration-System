# creating a main function to test the validate_user function
def main():
    # creating a dictionary to store the registered users
    registered_users = {}
    # creating a loop to keep asking for user input
    while True:
        # asking for user input
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")