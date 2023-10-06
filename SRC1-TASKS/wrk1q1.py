total = 0
#Array Declaration
num = [0 for _ in range(6)]
for i in range(6):
    num[i] = int(input("Enter num:"))
    total = total + num[i]
#next i
for i in range(5,-1,-1):
    print(num[i])
#next i
print("Total:",total)
print("Average:",total/6)