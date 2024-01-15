alist = [1, 3, 4, 6, 8, 9]
blist = [2,5,12,14,17]
clist = [0 for _ in range(len(alist)+len(blist))]
def mergeSort2(alist):
    if len(alist) > 1:
        mid = len(alist) // 2       # performs integer division
        lefthalf = alist[:mid]      # left half of alist put into lefthalf
        righthalf = alist[mid:]     # right half of alist put into righthalf
        merge(alist,lefthalf,righthalf)
        print("Merged sublist ",alist)
    #endif        
#endprocedure
#*********** MAIN PROGRAM ***************

def merge(clist, alist, blist):
    newlistindex = 0
    alistindex = 0
    blistindex = 0
    while alistindex < len(alist) and blistindex < len(blist):
        if alist[alistindex] <= blist[blistindex]:
            clist[newlistindex] = alist[alistindex]
            newlistindex += 1
            alistindex += 1
        else:
            clist[newlistindex] = blist[blistindex]
            newlistindex += 1
            blistindex += 1
        #end if
    #end while
    if alistindex == len(alist):
        while blistindex < len(blist):
            clist[newlistindex] = blist[blistindex]
            newlistindex += 1
            blistindex += 1
        #end while
    elif blistindex == len(blist):
        while alistindex < len(alist):
            clist[newlistindex] = blist[blistindex]
            newlistindex += 1
            blistindex += 1
        #end while
    #end if
#end procedure
merge(clist,alist,blist)
print(clist)

alist = [3, 1, 9, 8, 4, 6]
print("Unsorted list: ",alist)
mergeSort2(alist)
print("Sorted list: ",alist)