#Gets user's number
num = input("Please input the time in the format hours:minutes:seconds")
#Replaces : in code to spaces
num = num.replace(":"," ")
#Splits the numbers into seperate variables in a list
num = num.split()
#Turns each part of the list into an integer
for x in range(0,len(num)):
    num[x] = int(num[x])
#Prints the time in seconds
print(num[0]*3600 + num[1]*60 + num[2])
