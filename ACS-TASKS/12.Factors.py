#Gets user's number
num = input("Please input your number")
#Turns user's input into an integer
num = int(num)
#Prints factors of user's number
for x in range(2,num):
    if num % x == 0:
        print(x)