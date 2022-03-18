import random

n = random.randint(1, 9)  # generating the random number
guess = 0
count = 0
while int(guess) != n:
    guess = input("Guess the number from 1 through 9!\n")
    if "exit" in guess:
        break
    elif int(guess) > n:
        print("Too High!")
    elif int(guess) < n:
        print("Too Low!")

    count += 1
if guess != str(n):
    beg = input("Quitter! I'll never tell you which number it was! You only tried " + str(count) + " times!\n ")
    if "please" or "pls" in beg:
        print("Ok it was " + str(n) + " ...")
else:
    print("Good job! the random number was " + str(n) + " and you got it in " + str(count) + " guesses!")
