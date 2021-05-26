
# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please Choose One Of 'Rock', 'Paper', 'Scissors': ")


if (user_choice == "Rock") or (user_choice == "Paper") or (user_choice == "Scissors"):
    print("Valid. Keep Going.")

else:
    print("OOPS, Invalid Input. Please try again.")
    EXIT()
valid_options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(valid_options)
print("Computer Choice: ", computer_choice)


print("THIS IS THE END OF THE GAME. PLEASE PLAY AGAIN.")