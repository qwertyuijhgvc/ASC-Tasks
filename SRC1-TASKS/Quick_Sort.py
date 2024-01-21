def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
#end procedure

def quickPass(arr):
    pivot =len(arr) -1
    ptr = 0
    direction = 1
    while ptr != pivot:
        if arr[ptr] < arr[pivot]:
            ptr += direction
        else:
            swap(arr,ptr,pivot)
            pivot,ptr = ptr,pivot
            direction = direction * -1
        #end if
    #end while
#end procedure

data = ["A","F","G","B","E","C","H","D"]
