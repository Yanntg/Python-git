import random
# random list sizes:
n1 = random.randint(1, 20)
n2 = random.randint(1, 20)
# generating the lists:
a = random.sample(range(1, 100), n1)
b = random.sample(range(1, 100), n2)

c = [i for i in a if i in b]  # list with the common numbers
print(c)
