
# game.py


import random
 
import os 

import dotenv

dotenv.load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME")


#introduction 

print("Rock, Paper, Scissors, Shoot!")
print("-------------------------------------------------------")
print("Welcome " + PLAYER_NAME + " to my Rocks, Paper, Scissors game." )
print("-------------------------------------------------------")

#playing the game
user_choice = input("Please Choose One Of 'Rock', 'Paper', 'Scissors': ")


#player's choice
if (user_choice == "Rock") or (user_choice == "Paper") or (user_choice == "Scissors"):
    print("-------------------------------------------------------")
    print("You chose: " + user_choice)
else:
    print("OOPS, Invalid Input. Please try again.")
    EXIT()

#computer choice
valid_options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(valid_options)
print("-------------------------------------------------------")
print("The computer chose: ", computer_choice)
print("-------------------------------------------------------")
# Determining winner: 

# Rock vs. Rock, Paper vs. Paper, Scissors vs. Scissors = tie
if(user_choice == computer_choice):
    print("Tie! Please play again.")

# Rock beats Scissors.

elif((user_choice == "Rock") and computer_choice == "Scissors"):
        print("You win! Way to go!")

elif((user_choice == "Scissors") and computer_choice == "Rock"):
        print("You lose! Better luck next time.")

# Paper beats Rock
elif((user_choice == "Paper") and computer_choice == "Rock"):
        print("You win! Way to go!")
elif((user_choice == "Rock") and computer_choice == "Paper"):
        print("You lose! Better luck next time.")

#Scissors beats Paper
elif((user_choice == "Scissors") and computer_choice == "Paper"):
        print("You win! Way to go!")

elif((user_choice == "Paper") and computer_choice == "Scissors"):
        print("You lose! Better luck next time.")

print("-------------------------------------------------------")


print("THIS IS THE END OF THE GAME. PLEASE PLAY AGAIN.")