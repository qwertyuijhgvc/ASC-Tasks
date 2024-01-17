numbers = [3,6,2,8,1]
def sum_recursive(array,length):
    if length == 0:
        return array[length]
    else:
        return array[length] + sum_recursive(array,(length -1))
#end function
def sum_iterative(array,length):
    total = 0
    for x in range(length+1):
        total += array[x]
    #next x
    return total
#end function
    
    
print(sum_recursive(numbers,4))
print(sum_iterative(numbers,4))