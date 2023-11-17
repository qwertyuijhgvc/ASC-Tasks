class Node:
    def __init__(self,data,pointer) -> None:
        self.data = data
        self.pointer = pointer
    #end constructor
    def __repr__(self) -> str:
        return "Data:"+self.data+",Ptr:"+str(self.pointer)

#end Node record
linked_list_data = []
linked_list_data.append(Node("Lucas",2))
linked_list_data.append(Node("A'yaan",0))
linked_list_data.append(Node("Suren",-1))
linked_list_data.append(Node("Empty",4))
linked_list_data.append(Node("Empty",-1))
def outputList(arr):
    global start_pointer
    current_pointer = start_pointer
    while current_pointer != -1:
        print(arr[current_pointer].data)
        current_pointer=arr[current_pointer].pointer
    #end while
#end procedure
start_pointer = 1
next_free_pointer = 3

print(linked_list_data)
