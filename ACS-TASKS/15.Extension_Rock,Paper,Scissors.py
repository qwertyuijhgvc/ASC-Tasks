import random
AIChoice = random.randint(1,3)
UserInput = ""
UserInput = input("R = Rock P = Paper S = Scissors ")
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