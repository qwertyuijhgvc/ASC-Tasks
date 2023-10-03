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
   print(caesar[x])
    
