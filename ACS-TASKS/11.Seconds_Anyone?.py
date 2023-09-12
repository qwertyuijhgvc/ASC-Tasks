num = input()
num = num.replace(":"," ")
num = num.split()
for x in range(0,len(num)):
    num[x] = int(num[x])
print(num[0]*3600 + num[1]*60 + num[2])
