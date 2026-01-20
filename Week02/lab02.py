import random

choices = ["Rock", "Paper", "Scissor"]

playerChoice = input("Enter your choice (1-Rock, 2-Paper, 3-Scissor):")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be between 1 and 3!")
    
else:
    ComputerChoice = random.randint(1,3)

    playerChoiceIndex = choices[playerChoice - 1] # ==> 0, 1, 2
    ComputerChoiceIndex = choices[ComputerChoice - 1]
    print(playerChoiceIndex, ComputerChoiceIndex)

    # Determine the winner logic using if/elif/else
    if playerChoice == ComputerChoice:
        print("It's a tie")
    elif playerChoice == 1 and ComputerChoice == 3:
        print("Rock beats scissor - you win!")
    elif playerChoice == 2 and ComputerChoice == 1:
        print("Paper beats Rock - you win!")
    else:
        print("You lose!")