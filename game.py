import random

choice = ["rock","paper","scissors"]

computer = random.choice(choice)
player = None

while player not in choice:
    player = input("rock, paper, or  scissors?: ").lower()
if player == computer:
    print("computer: ",computer)
    print("player: ",player)
    print("tied!")
elif player == "rock":
    if computer == "paper": 
     print("computer: ",computer)
    print("player: ",player)
    print("you lose!")
    if  computer == "scissors": 
            print("computer: ",computer)
    print("player: ",player)
    print("you win!")
elif player == "rock":
    if computer == "paper": 
            print("computer: ",computer)
    print("player: ",player)
    print("you lose!")
    if  computer == "rock": 
            print("computer: ",computer)
    print("player: ",player)
    print("you win!")
    