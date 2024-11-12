import re

def validate_email(email):
    # Regular expression for validating an email address
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return "Valid email address."
    else:
        return "Invalid email address."

if __name__ == "__main__":
    email = input("Enter an email address to validate: ")
    print(validate_email(email))
#This tool checks if an email address is valid or not by using regular expressions. It’s useful for filtering fake or invalid email inputs.#