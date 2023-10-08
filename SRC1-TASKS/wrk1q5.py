def grid_print():
    cord_x = int(input("Enter x co-ordiante "))
    cord_y = int(input("Enter y co-ordiante "))
    grid_array = [ ["X"]*4 for i in range(6)]
    grid_array[cord_x][cord_y] = "O"
    for y in range(6):
        print(grid_array[y])
#end function
while True:
    grid_print()
#end while