def linearSearch(array, item): #function
    _ = 0 
    while array[_] != item and item < len(array):
        _ += 1
    #end while
    if item >= len(array):
        return False
    else:
        return _
    #end if
#end function
testArray = [10,2,4,3,8]  
print(linearSearch(testArray, 4))
