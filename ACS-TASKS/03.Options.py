# Gives a starting value to variable num
num = 0
# While loop to keep asking for value if inputted value is invalid
while num > 3 or num <= 0:
    print("Please select option number between 1 and 3")
    num = int(input())
# end while
# Print out option user selected
print("You have selected option " + str(num))
    
