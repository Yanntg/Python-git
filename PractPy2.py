num = int(input("Pick a number!\n"))  # Requests the number
check = int(input("Pick another number and I'll tell you if the first number is a multiple of the second!\n"))  # For the
# extras, solves the initial problem if check = 2

if num % check > 0:  # if used to check multiplicity.
    print(str(num) + " is NOT a multiple of " + str(check) + "!!")  # Gives answer
else:
    print(str(num) + " IS a multiple of " + str(check) + "!!")  # Gives answer
