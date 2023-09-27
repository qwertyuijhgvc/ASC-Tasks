
def displayMenu():
    namelist = [""] * 10 
    choice = 0
    loop = True
    while (loop):
        print("1   Add Name")
        print("2   Display List")
        print("3   Quit")
        choice = int(input("Enter Your Choice "))
        while (choice > 3) or (choice < 1):
            if (choice > 3) or (choice < 1):
                choice = int(input("Invalid choice - please re-enter "))
        if (choice == 1):
            nameChange(namelist)
        elif (choice == 2):
            display(namelist)
        elif (choice == 3):
            print("Program Terminating")
            loop = False
            
    
def nameChange(list):
    name = input("Enter the name to be added to the list ")
    place = int(input("Enter the position in the list to insert the name (1-10) "))
    list[place] = name
def display(list):
    print(list)
    






displayMenu()
    
