class Node:
    def __init__(self, name, pointer) -> None:
        self.name = name
        self.pointer = pointer

    def __repr__(self) -> str:
        return "Data:" + self.name + ", Ptr:" + str(self.pointer)

# Create an array of blank Nodes (records)
myList = [Node("", -1) for _ in range(6)]
for index in range(6):
    myList[index].pointer = index + 1

# Set the last element's pointer to -1
myList[5].pointer = -1

start_pointer = -1
next_free = 0


def outputList(arr):
    global start_pointer
    current_pointer = start_pointer
    while current_pointer != -1:
        print(arr[current_pointer])
        current_pointer = arr[current_pointer].pointer


def AddItem(newName, myList):
    global next_free
    global start_pointer
    if next_free == -1:
        print("Error")
    else:
        myList[next_free].name = newName
        if start_pointer == -1:
            temp = myList[next_free].pointer
            myList[next_free].pointer = -1
            start_pointer = next_free
            next_free = temp
        else:
            p = start_pointer
            if newName < myList[p].name:
                myList[next_free].pointer = start_pointer
                start_pointer = next_free
            else:
                place_found = False
                while myList[p].pointer != -1 and not place_found:
                    if newName >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        place_found = True
                temp = next_free
                next_free = myList[next_free].pointer
                myList[temp].pointer = myList[p].pointer
                myList[p].pointer = temp
                
                
def RemoveItem(name_to_remove, myList):
    global start_pointer
    global next_free
    if start_pointer == -1:
        print("Error: List is empty")
        return
    p = start_pointer
    prev = None
    while p != -1 and myList[p].name != name_to_remove:
        prev = p
        p = myList[p].pointer
    if p == -1:
        print(f"Error: Item '{name_to_remove}' not found")
        return
    if prev is None:
        start_pointer = myList[p].pointer
    else:
        prev_pointer = myList[prev].pointer
        myList[prev].pointer = myList[p].pointer
    myList[p].pointer = next_free
    next_free = p

AddItem("Colin", myList)
AddItem("Albert", myList)
AddItem("Barry", myList)
AddItem("Derek", myList)
AddItem("Fred", myList)
AddItem("Trevor", myList)
print(myList)
