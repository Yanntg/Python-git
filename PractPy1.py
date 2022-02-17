name = input("Enter your name and age:")  # asks both infos in the same message
age = int(input(""))  # age will be inputted after the name and pressing enter
year = 2022 + (100 - age)  # math
message = "hello " + name + "! you'll turn 100 years old at year " + str(year)  # useful for the extras
print(message + "\n")  # first part done

# extras

n = int(input("Choose a number:"))  # number of times the message will be repeated
print(message * n + "\n")  # prints the message that many times

# second part done
# third part

for i in range(n):  # using "for" to create the repetition
    print(message + "\n")  # printing

    # done
