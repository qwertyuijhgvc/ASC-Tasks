#Main procedure that loops the display screen until user input 3
def displayMenu():
    #Sets variable values
    namelist = [""] * 10 
    choice = 0
    loop = True
    while (loop):
        print("1   Add Name")
        print("2   Display List")
        print("3   Quit")
        #Gets user input for chocie
        choice = int(input("Enter Your Choice "))
        #Validates user input
        while (choice > 3) or (choice < 1):
            if (choice > 3) or (choice < 1):
                choice = int(input("Invalid choice - please re-enter "))
            #End If
        #End while
        #Calls subroutines depending on user choice or ends program
        if (choice == 1):
            nameChange(namelist)
        elif (choice == 2):
            display(namelist)
        elif (choice == 3):
            print("Program Terminating")
            loop = False
        #End If
    #End while
#End subroutine
#Subroutine to change value in list
def nameChange(list):
    name = input("Enter the name to be added to the list ")
    place = int(input("Enter the position in the list to insert the name (1-10) "))
    list[place] = name
#End subroutine
#Displays full list of names
def display(list):
    print(list)
#End subroutine
#Main program calls subroutine
displayMenu()
    
