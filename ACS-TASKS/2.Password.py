# This asks the user to input their password
print("Please input your password (It must be longer than 6 characters)")
# Change password varaible to user input
password = input("")
# If statement to check if the inputted password is valid
if len(password) >= 6:
    print("Password is valid")
else:
    print("Password is invalid")
# end if