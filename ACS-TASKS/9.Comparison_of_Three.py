#Gets users input of three numbers
num = [0]* 3
for x in range(0,len(num)):
    num[x] = int(input("Please input a number"))
#Sorts then prints users numbers in descending order
num.sort(reverse=True)
print(num)