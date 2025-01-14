def binarySearch(array, item):
    index = int(len(array)/2)
    while array[index] != item and index >= 0  and index < len(array):
        if array[index] > item:
            index = int(index/2)
        elif array[index] < item:
            index = int((index+(len(array)-1))/2)
        #end if
    #end while
    return index
#end function
def binarySearch(array, item, high, low):
    if low > high:
        return False
    #end if
    