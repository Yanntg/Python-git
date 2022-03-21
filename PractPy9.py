import random

n = random.randint(1, 9)  # generating the random number
guess = 0  # the guess starts as any number != n
count = 0  # this is the guess count, to be printed at the end
while int(guess) != n:
    guess = input("Guess the number from 1 through 9!! Or type exit \n")  # stores the user guess
    if "exit" in guess:  # if the user wants to quit
        break
    elif int(guess) > n:  # if guess is higher than the number
        print("Too High!")
    elif int(guess) < n:  # if guess is lower than the number
        print("Too Low!")

    count += 1  # after the guess, count is increased by one
if guess != str(n):  # if this happens, the user exited the loop without guessing it right
    beg = input("Quitter! I'll never tell you which number it was! You only tried " + str(count) + " times!\n ")
    if "please" or "pls" in beg:  # easter egg
        print("Ok it was " + str(n) + " ...")
else:
    print("Good job! the random number was " + str(n) + " and you got it in " + str(count) + " guesses!")
