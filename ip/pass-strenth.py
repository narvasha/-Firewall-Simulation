import string

def password_strength(password):
    if (len(password) >= 8 and 
        any(c.isupper() for c in password) and 
        any(c.islower() for c in password) and 
        any(c.isdigit() for c in password) and 
        any(c in string.punctuation for c in password)):
        return "Strong"
    return "Weak"

password = input("Enter a password to check: ")
print(password_strength(password))
