import random

def random_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

win = 0
loss = 0
tie = 0

amount_of_games = int(input("How many times do you want to play: "))

for i in range(amount_of_games):
    computer = random_choice()
    human = str(input("Choose rock, paper, or scissors: "))

    if human == "scissors" and computer == "rock":
        loss += 1
    elif human == "scissors" and computer == "paper":
        win += 1
    elif human == "scissors" and computer == "scissors":
        tie += 1
    elif human == "rock" and computer == "rock":
        tie += 1
    elif human == "rock" and computer == "paper":
        loss += 1
    elif human == "rock" and computer == "scissors":
        win += 1
    elif human == "paper" and computer == "rock":
        win += 1
    elif human == "paper" and computer == "paper":
        tie += 1
    elif human == "paper" and computer == "scissors":
        loss += 1

print(f"\n\nRock Paper Scissors Final Scores\n\nWins: {win}\nTies: {tie}\nLosses: {loss}")
