# Asks user for a number between 100 and 999
print("Please enter a number between 100 and 999")
# Gets users input
num = int(input())
# Sets variables with values for the hundreds tens and units for the user value
hundreds = num // 100
tens = (num - hundreds * 100) // 10
units = (num - hundreds * 100 - tens *10) 
# Prints the hundreds tens and units variables
print(hundreds ,"hundreds", tens,"tens", units,"units")
