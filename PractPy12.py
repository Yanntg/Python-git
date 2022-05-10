def getlist():  # the user will input the list
    l1 = []
    while 1:  # repeat until the user chooses to stop
        last = input("Pick a number(type stop when you're done)!\n")
        if last == "stop":
            break  # if the input is 'stop' the function ends and return the user list, l1
        else:
            l1.append(int(last))

    return l1


def ends(l1):  # simple function to get starting and end numbers of the list and print them inside a new list
    l2 = [l1[0], l1[-1]]
    print(l2)


# just use both functions:
ends(getlist())