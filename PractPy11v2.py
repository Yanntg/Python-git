import math  # used only to make the code a little quicker


def checkprime(x):  # function that will check if input x is prime or not, also prints its smaller divisor bigger than 1
    p = 1  # if at the end of the function p still equals 1, x is prime
    for i in range(2, 1 + math.floor(math.sqrt(x))):  # only tests up to the floor of sqrt(x), its enough
        if x % i == 0:  # if this happens, x is not prime
            print("Not prime! " + str(i) + " divides " + str(x))
            p = 0
            break  # stops testing as soon as the first divisor is found
    if p == 1:
        print("Prime!")
    return p


def getdiv(x):
    div = [i for i in range(1, x+1) if x % i == 0]  # getting its divisors, same as exercise 4
    return div


n = int(input("Pick a number!\n"))  # stores number
if checkprime(n) == 0:  # this line already prints checkprime's texts
    r = input("Do you want to know all its divisors?")
    if "y" in r:
        print(getdiv(n))
else:
    print("ok bye")  # all my codes are very polite, thank you
