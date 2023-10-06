MAX = 12
name_array = ["" for _ in range (MAX)]
request = input("Enter student name ")
found = False
index = 0
name_array[0] = "Luke"
name_array[1] = "bob"
name_array[2] = "jerry"
while not found and index < MAX:
    if(name_array[index] == request and index < MAX):
        print("Student record is in " + str(index + 1))
        found = True 
    #end if
    index += 1
#end while
if index == MAX:
    print("Student record not found")
#end if
    