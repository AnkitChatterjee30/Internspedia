import random
import math
name=input("Enter your name : ")
lower=int(input("Enter the lower limit : "))
higher = int(input("Enter the higher limit : "))
randNumber= random.randint(lower, higher)
guesses=0
userGuess=None
print(f"Hello {name}, play the game by guessing the number between {lower} and {higher} inclusive range.\nYou have {round(math.log(higher-lower+1,2))} guesses")
while(guesses<(math.log(higher-lower+1,2))):
    userGuess = int(input(f"{name}, enter your Guess :"))
    guesses+=1
    if (userGuess==randNumber):
        print(f"Congratulations {name}!, you guessed the exact  number. ")
        print(f"You guessed it in just {guesses} guesses.")
        break
    else: 
        if (userGuess>randNumber):
            print(f"Sorry, {name}, you guessed it wrong! Enter a lower number")
            print(f"You have used {guesses} guesses. You just have {round(math.log(higher-lower+1,2))-guesses} left.")
        else:
            print(f"Sorry, {name}, you guessed it wrong! Enter a higher number")
            print(f"You have used {guesses} guesses. You just have {round(math.log(higher-lower+1,2))-guesses} left.")
        if guesses==round(math.log(higher-lower+1,2)) and userGuess!=randNumber:
            print(f"Unfortunately {name}, you couldn't guess the number correctly in {guesses} guesses.\nIt was {randNumber}.\nBetter luck next time.")
            break