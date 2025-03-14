import random

def getChoices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

def checkWin (player, computer):
    print(f"You chose {player}, computer chose {computer}.")

    """
    if player == computer:
        return "It is a tie"
    elif player == "rock":
        if computer == "paper":
            return "Paper wraps rock. You lose..."
        else:
            return "Rock smashes scissors. You Win!!"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper. You lose..."
        else:
            return "Paper warps rock. You Win!!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors. You lose..."
        else:
            return "Scissors cuts paper. You Win!!"

    """

   
    if player == computer:
        return "It is a tie"
    elif player == 'rock' and computer =='scissors':
        return "Rock smashes scissors! You win!"
    elif player == 'paper' and computer =='rock':
        return "Paper wraps the rock! You win!"
    elif player == 'scissors' and computer =='paper':
        return "Scissors cuts paper ! You win!"
    else:
        return "You Lost"
   
    
choices = getChoices()
result = checkWin(choices['player'], choices ['computer'])
print(result)