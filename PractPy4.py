n = int(input("Pick a number!\n"))  # requests the number
print([i for i in range(1, n+1) if n % i == 0])  # using the same trick from the previous exercise to do it in one line
