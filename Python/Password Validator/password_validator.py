# SIMPLE PYTHON PASSWORD VALIDATOR
# REQUIRMENTS FOR A PASSWORD TO BE VALID:
#                AT LEAST 8 CHAR LONG
#                CONTAIN ANY SORT OF LETTERS, NUMBERS , AND CHARACTERS $%#@
#                HAS TO END WITH A NUMBER


import re


def password_checker():
    pattern = re.compile(r"([A-Za-z0-9$%#@]){8,}\d")
    password = input("Please provide a password to check!\n")
    check = pattern.fullmatch(password)
    if check:
        print(f"Password '{password}' has good format!")
    else:
        print(f"password '{password}' doesn't respect the corect format!")


password_checker()
