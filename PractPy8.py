import os

replay = "yes"
p1 = "none"
p2 = "none"
p1w = "Player 1 wins!"
p2w = "Player 2 wins!"
while replay == "yes":  # for the replayability

    # p1 loop:
    while p1 != "rock" or p1 != "paper" or p1 != "scissors":
        p1 = input("player 1, choose rock, paper or scissors:")  # user input 1
        if p1 == "rock" or p1 == "paper" or p1 == "scissors":  # checks if p1 typed in correctly
            break  # if everything is ok, break out of p1 loop
        else:
            print("input not recognised!")  # if p1 typed incorrectly, prints message and restart this loop

    # clearing the terminal so player 2 doesnt cheat!!
    os.system('cls' if os.name == 'nt' else 'clear')  # works for linux windows and mac: nt means windows

    # p2 loop:
    while p2 != "rock" or p2 != "paper" or p2 != "scissors":
        p2 = input("player 2, choose rock, paper or scissors:")  # user input 2
        if p2 == "rock" or p2 == "paper" or p2 == "scissors":  # checks if p2 typed in correctly
            break  # if everything is ok, break out of p2 loop
        else:
            print("input not recognised!")  # if p2 typed incorrectly, prints message and restart this loop

# results:
    if p1 == p2:
        print("TIE!")
    else:
        if p1 == "rock":
            if p2 == "paper":
                print(p2w)
            elif p2 == "scissors":
                print(p1w)
        elif p1 == "paper":
            if p2 == "rock":
                print(p1w)
            elif p2 == "scissors":
                print(p2w)
        elif p1 == "scissors":
            if p2 == "rock":
                print(p2w)
            elif p2 == "paper":
                print(p1w)
    p1 = "none"
    p2 = "none"
    replay = input("play again?(yes/no)")