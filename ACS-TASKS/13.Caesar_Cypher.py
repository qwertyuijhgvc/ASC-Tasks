line = input("Enter your line ")
line = line.lower()
line = line.replace(" ","")
letters = [*line]
print(letters)
caesar = [0] * 100000000
coded = ""
for x in range(0, len(letters)):
   caesar[x] = ord(letters[x]) 
   if caesar[x] == 121:
       caesar[x] = 97
   else:
       caesar[x] = caesar[x] + 2
   caesar[x] = chr(caesar[x])
   coded += caesar[x]
print(coded)
