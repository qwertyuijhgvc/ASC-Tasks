num = input()
num = int(num)
for x in range(2,num):
    if num % x == 0:
        print(x)