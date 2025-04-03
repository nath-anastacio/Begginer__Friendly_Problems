#Rock Paper Scissors Game in Python

import random
import os
import re

#Clean the console screen based on the operating system
os.system('cls' if os.name=='nt' else 'clear')

#Main game loop - runs indefinitely until manually terminated
while (1 < 2):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")

    #Get the user's choice, store it, and validate it using regular expression
    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper.")

    # Display the user's choice
    print ("You chose: " + userChoice)

    #Randomly select the computer's choice and displays it
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print ("I chose: " + opponenetChoice)

    #Determine the winner based on the games rules
    if opponenetChoice == str.upper(userChoice) and str.upper(userChoice) == "P":
        print ("Tie! ")
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':
        print ("Rock beat scissors, I win! ")
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':
        print ("scissors beat paper, I win! ")
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':
        print ("Paper beat rock, I win!")
    else:
        print ("You win!")
