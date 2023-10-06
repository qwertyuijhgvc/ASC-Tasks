Outlet1Sales = [10, 12,15,10]
Outlet2Sales = [5,8,3,6]
Outlet3Sales = [10,12,15,10]
total = 0
for x in range (4):
    total = Outlet1Sales[x] + Outlet2Sales[x] + Outlet3Sales[x]
    print("Total for quarter" , x+1, total)