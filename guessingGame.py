print("Number Guessing Game")
A = int(input("Guess a number between 1 and 9 :- "))
if (A < 4):
    B = int(input("Your Guess was too low, Guess a number greater than 3 :- "))
elif (A < 10):
    print("Guess a number lower than 10")
else :
    print("Please Enter a valid number")
if (B < 5):
    C = int(input("Your Guess was too low, Guess a number greater than 4 :- "))
elif (B < 10):
    print("Guess a number lower than 10")
else :
    print("Please Enter a valid number")
if (C < 8):
    D = int(input("Your Guess was too low, Guess a number greater than 7 :- "))
elif (C < 10):
    print("Guess a number lower than 10")
else :
    print("Please Enter a valid number")
if (D == 8):
    print("Congratulations You Won The Game , You Are Guessing Master ! ")
elif (D != 8):
    print("You Lose")
else :
    print("Please Enter a valid number")