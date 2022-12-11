########################################################### SIMPLE PASSWORD LENGTH CHECKER IN PYTHON ############################################################
########################################################### SIMPLE PASSWORD LENGTH CHECKER IN PYTHON ############################################################
########################################################### SIMPLE PASSWORD LENGTH CHECKER IN PYTHON ############################################################

username = input("Provide your username\n")
password = input("Provide your password\n")

password_length = len(password)
hidden_password = '*' * password_length

print(f"{username}, your password, {hidden_password}, is {password_length} letters long!")