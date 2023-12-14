def binarySearch(aList, itemSought):
    found = False
    index = -1
    first = 0
    last = len(aList) -1
    while first <= last and found == False:
        midpoint = (first+last) // 2
        if aList[midpoint] == itemSought:
            found = True
            index = midpoint
        else:
            if aList[midpoint] < itemSought:
                first = midpoint
                midpoint = (first+last) // 2
            elif aList[midpoint] > itemSought:
                last = midpoint
                midpoint = (first+last) // 2
            #end if
        #end if
    #end while
    return index
#end function
fillerList = [2,5,10,28,67,100,150]
print(binarySearch(fillerList,10))

