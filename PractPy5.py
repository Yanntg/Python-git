import random
# generating the lists size randomly:

x1 = random.randint(1, 10)
x2 = random.randint(1, 10)
# generating the random lists:

list1 = random.sample(range(1, 30), x1)
list2 = random.sample(range(1, 30), x2)
# printing the results:

print("list 1: " + str(list1))
print("list 2: " + str(list2))
print("repeated numbers: " + str([i for i in list1 if i in list2]))
