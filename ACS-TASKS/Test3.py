list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
mergelist = list1 + list2
for i in range(len(mergelist)):
    for j in range(i + 1, len(mergelist)):

        if mergelist[i] > mergelist[j]:
           mergelist[i], mergelist[j] = mergelist[j], mergelist[i]
    #next j
#next i
print(mergelist)
