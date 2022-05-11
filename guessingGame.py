import random
A = random.randint(1,9)
print("Number Guessing Game")
chances = 0
while chances < 5:
    B = int(input("Enter a number between 1 and 9 :- "))
    if A == B :
        print("Correct")
        break
    else :
        print("Incorrect")
    chances += 1
