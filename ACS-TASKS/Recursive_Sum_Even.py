def Sum_Even(n):
    total = 0
    if n > 0 and n % 2 == 0:
        total = n + Sum_Even(n-2)
    #end if
    return total
#end function
print(Sum_Even(8))
