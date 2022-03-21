import random
print(set(random.sample(range(1, 100), random.randint(1, 20))).intersection(set(random.sample(range(1, 100), random.randint(1, 20)))))
