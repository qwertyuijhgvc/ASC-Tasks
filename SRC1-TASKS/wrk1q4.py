outletSales = [ [0]*50 for i in range(4)]

total = [0,0,0,0]
outletSales[1][29] = 10
outletSales[2][29] = 50
outletSales [1][39] = 9
outletSales[3][36] = 8
outletSales[2][29] = 60
for quarter in range(4):
    for outlet in range(50):
        total[quarter] += outletSales[quarter][outlet]
    #next outlet
#next quarter
for _ in range(4):
    print(total[_])