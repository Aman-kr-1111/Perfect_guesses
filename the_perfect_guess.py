#   Project 2 ---> The perfect guess

import random
randNumber=random.randint(1,100)
userGuess=None
guess=0
name=input("Enter your name : ")
while(userGuess!=randNumber):
    userGuess=int(input("Enter your guess number(1 to 100) : "))
    guess+=1
    if(userGuess==randNumber):
        print("\nYou guessed it right!")
    else:
        if(userGuess>randNumber):
            print("\nYou guessed it wrong! Enter a smaller number")
        else:
            print("\nYou guessed it wrong! Enter a larger number")

print(f"\n{name} guessed the number in {guess} guesses")

