# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
choices = ["Rock", "Paper", "Scissor"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0

while True:


    player = input("Choose: Rock,Paper or Scissor? ").capitalize()

    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!", computer, "covers", player)
            cpu_score += 1
        else:
            print("You Win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissor":
            print("You Lose!", computer, "cut", player)
            cpu_score += 1
        else:
            print("You Win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissor":
        if computer == "Rock":
            print("you lose!", computer, "smashes", player)
            cpu_score += 1
        else:
            print("You Win", player, "cuts", computer)
            player_score += 1
    elif player == "End":
        print("Final Scores: ")
        print("CPU:{}".format(cpu_score))
        print("Player:{}".format(player_score))
        break






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
