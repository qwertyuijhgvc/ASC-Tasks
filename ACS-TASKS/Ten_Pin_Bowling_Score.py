#Create lists and variables to hold bowling scores
bowl1 = [0] * 100
bowl2 = [0] * 100
Score = 0
#To get input of number of pins knocked down
for x in range (0,10):
    bowl1[x] = int(input("How many pins did you knock down in game " + str(x+1) + " "))
    #Validation of input
    while (bowl1[x] > 10):
        bowl1[x] = int(input("Invalid input! Please input a number between 1 and 10 (inclusive) "))
    #End while
    if bowl1[x] != 10:
        bowl2[x] = int(input("How many more pins did you knock down "))
    #Validation of input
    while (bowl2[x] + bowl1[x] > 10):
        bowl2[x] = int(input("Invalid input the total cannot be more than 10! Please input a valid number "))
    #End while
    #End if
#Next x
#To get input of the extra bowls if their is a strike or spare on the final frame
if bowl1[9] == 10:
    bowl1[10] = int(input("What did you get in extra Frame 1 "))
    #Validation of input
    while (bowl1[10] > 10):
        bowl1[10] = int(input("Invalid input! Please input a number between 1 and 10 (inclusive) "))
    #End while
    bowl1[11] = int(input("What did you get in extra Frame 2 "))
    #Validation of input
    while (bowl1[11] > 10):
        bowl1[11] = int(input("Invalid input! Please input a number between 1 and 10 (inclusive) "))
    #End while
#End if
if bowl1[9] + bowl2[9] == 10 and bowl1[9] != 10:
    bowl1[10] = int(input("What did you get in extra Frame 1 "))
    #Validation of input
    while (bowl1[10] > 10):
        bowl1[10] = int(input("Invalid input! Please input a number between 1 and 10 (inclusive) "))
    #End while
#End if
#To calculate extra score given on spares
for x in range(0,9):
    if bowl1[x] + bowl2[x] == 10:
        Score += bowl1[x+1]
    #End if
        if bowl1[x] == 10:
            Score -= bowl1[x+1]
        #End if
#Next x
#To calculate extra score on strikes
for x in range (0,9):
    if bowl1[x] == 10:
        bowl1[x] = bowl1[x] + bowl1[x+1]
    #End if
        if bowl1[x+1] == 10:
            bowl1[x] = bowl1[x] +bowl1[x+2]
        else:
            bowl1[x] = bowl1[x] +bowl2[x+1] 
        #End if
#Next x       
#To add up the score
for x in range(0,12):
    Score += bowl1[x] + bowl2[x]
#Next x
#To print the final score
print(Score)