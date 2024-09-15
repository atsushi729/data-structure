"""
Write a Python program to check that a password has a capital letter, a
special character (: ; !) and a number.
"""


def check_valid_password(password: str) -> bool:
    return (
            any(c.isupper() for c in password) and
            any(c in ":;!@#$%^&*()_+" for c in password) and
            any(c.isdigit() for c in password)
    )


password = "Password123!"
password1 = "password123!"
password2 = "password123"
password3 = "Password123"

print(check_valid_password(password))  # True have a capital letter, a special character and a number
print(check_valid_password(password1))  # False don't have a capital letter
print(check_valid_password(password2))  # False don't have a special character
print(check_valid_password(password3))  # False don't have a special character and a number
