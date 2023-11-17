class Node:
    def __init__(self,name,pointer) -> None:
        self.name = name
        self.pointer = pointer
    #end constructor
    def __repr__(self) -> str:
        return "Data:"+self.name+",Ptr:"+str(self.pointer)
#end Node record
# Create array of blank Nodes (records)
myList = [Node("",-1) for _ in range(50) ]
for index in range(49):
    myList[index].pointer = index + 1
#next index
myList[49].pointer = -1
start = -1
nextfree = 0
print(myList)

def outputList(arr):
    global start_pointer
    current_pointer = start_pointer
    while current_pointer != -1:
        print(arr[current_pointer].data)
        current_pointer=arr[current_pointer].pointer
#end function


def AddItem(newName,myList):
    global nextfree
    global start
    if nextfree == -1:
        print("Error")
    else:
            myList[nextfree].name = newName
            if start == -1: 
                temp = myList[nextfree].pointer     
                myList[nextfree].pointer = -1
                start = nextfree
                nextfree = temp
            else:
                p = start
                if newName < myList[p].name: 
                    myList[nextfree].pointer = start
                    start = nextfree
                else:    
                    placeFound = False
                    while myList[p].pointer != -1 and placeFound == False:
                        if newName >= myList[myList[p].pointer].name:
                            p = myList[p].pointer
                        else:
                            placeFound = True
                        #endif
                    #endwhile
                    temp = nextfree
                    nextfree = newName[nextfree].pointer
                    newName[temp].pointer = newName[p].pointer
                    newName[p].pointer = temp
                #endif
            #endif
       #endif
    #endprocedure

AddItem("Colin",myList)
AddItem("Albert",myList)
print(myList)
AddItem("Barry",myList)
AddItem("Derek",myList)
AddItem("Fred",myList)
outputList(myList)
AddItem("Trevor",myList)
