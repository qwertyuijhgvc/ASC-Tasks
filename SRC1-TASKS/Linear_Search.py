def linear_search(array, item):
    found = False
    index = 0
    while not found:
        if array[index] == item:
            found = True
        else:
            index += 1 
        #end if
        if index == len(array):
            index = -1
            found = True
    #end while
    return index
    #end if
#end function