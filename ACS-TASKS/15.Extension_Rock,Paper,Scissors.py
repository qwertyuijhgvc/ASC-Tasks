#Imports Random function
import random
#Gets the programs random RPS choice
AIChoice = random.randint(1,3)
#Gets user's RPS choice
UserInput = input("R = Rock P = Paper S = Scissors ")
#Sees who wins, loses or draws in RPS
if AIChoice == 1 and UserInput == "P":
    print("You win")
elif AIChoice == 2 and UserInput == "S":
    print("You win")
elif AIChoice == 3 and UserInput == "R":
    print("You win")
elif AIChoice == 1 and UserInput == "S":
    print("You lose")
elif AIChoice == 2 and UserInput == "R":
    print("You lose")
elif AIChoice == 3 and UserInput == "P":
    print("You lose")
else:
    print("Draw")