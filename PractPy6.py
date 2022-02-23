pal = input("Test for palindromes! Type your word:\n")  # user input
test = pal[::-1]  # starting point is the last element in the list and finishing point is the first
# comparing both lists:
if pal in test:
    print(str(pal) + " is a palindrome!")
else:
    print(str(pal) + " is NOT a palindrome!")
