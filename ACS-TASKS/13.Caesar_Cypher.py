#Gets user's input
line = input("Enter your line ")
#Changes input into lower case and removes spaces
line = line.lower()
line = line.replace(" ","")
#Puts users input into a list
letters = [*line]
#Creates a list variable and string variable
caesar = [0] * 100000000
coded = ""
#Puts ASCII values of user's input into a list
for x in range(0, len(letters)):
   caesar[x] = ord(letters[x]) 
   if caesar[x] == 121:
       caesar[x] = 97
   elif caesar[x] == 122:
       caesar[x] = 98
   else:
#Shifts the ASCII value by 2 
       caesar[x] = caesar[x] + 2
#Turns the ASCII values in list back to characters
   caesar[x] = chr(caesar[x])
#Turns list back into 1 string
   coded += caesar[x]
#Prints coded version of user input
print(coded)
