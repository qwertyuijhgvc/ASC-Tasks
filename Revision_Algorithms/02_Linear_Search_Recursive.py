def linearSearchRecursive(array, item, index): #function
    if index >= len(array):
        return False
    if array[index] == item:
        return index
    else:
        return linearSearchRecursive(array, item, index+1)
    #end if
#end function
testArray = [10,2,4,3,8]  
print(linearSearchRecursive(testArray, 4, 0))