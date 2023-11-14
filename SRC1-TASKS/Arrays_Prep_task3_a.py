school_input = 0
school = ["AAAA","BBBB","CCCC","DDDD"]
medal = [4,7,1,3]
while school_input != -1:
    school_input = int(input("Please enter a school number "))
    if school_input < 5 and school_input > 0:
        medal[school_input -1] += 1
    elif school_input == -1:
        for x in range(4):
            print("School number", x+1, "School name",school[x],"Number of medals", medal[x])
        #next x
    else:
        print("Invalid input")
    #end if
#end while