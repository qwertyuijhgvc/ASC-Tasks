
car_park_array = [ ["empty"]*10 for i in range(6)] 
car_number = input("Input car number ")
def validatey():
    validation = True
    while validation:
        space_y = int(input("Input y co-ordiante "))
        if space_y < 1 or space_y > 6:
            print("Invalid input! Please input a number 1-6 ")
        else:
            validation = False
            return(space_y)
        #end if
    #end while
#end function
def validatex():
    validation = True
    while validation:
        space_x = int(input("Input x co-ordiante "))
        if space_x > 10 or space_x < 1:
            print("Invalid input! Please input a number 1-10 ")
        else:
            validation = False
            return(space_x)
        #end if
    #end while
#end function
x_cord = validatex()
y_cord = validatey()
available_space = True
while available_space:
    if car_park_array[x_cord - 1][y_cord -1] == "empty":
        car_park_array[x_cord - 1][y_cord -1] = car_number
        available_space = False
    else:
        print("This space is taken")
        x_cord = validatex()
        y_cord = validatey()
    #end if
#end while
print(car_park_array)