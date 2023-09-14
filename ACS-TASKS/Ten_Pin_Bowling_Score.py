bowl1 = [0] * 100
bowl2 = [0] * 100
Score = 0
for x in range (0,10):
    bowl1[x] = int(input("How many pins did you knock down "))
    if bowl1[x] != 10:
        bowl2[x] = int(input("How many more pins did you knock down "))
if bowl1[9] == 10:
    bowl1[10] = int(input("What did you get in extra Frame 1 "))
    bowl1[11] = int(input("What did you get in extra Frame 2 "))
if bowl1[9] + bowl2[9] == 10:
    bowl1[10] = int(input("What did you get in extra Frame 1 "))
for x in range(0,9):
    if bowl1[x] + bowl2[x] == 10:
        Score += bowl1[x+1]
for x in range (0,9):
    if bowl1[x] == 10:
        bowl1[x] = bowl1[x] + bowl1[x+1]
        if bowl1[x+1] == 10:
            bowl1[x] = bowl1[x] +bowl1[x+2]
        else:
            bowl1[x] = bowl1[x] +bowl2[x+1] 
for x in range(0,12):
    Score += bowl1[x] + bowl2[x]
print(Score)
        
