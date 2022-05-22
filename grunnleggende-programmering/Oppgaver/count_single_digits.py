import random

random_list = []
for i in range(0, 1000):
    n = random.randint(0, 10)
    random_list.append(n)


for i in range(0, 10):
    counts = random_list.count(i)
    if counts != 0 and counts == 1:
        print(f'{i} occurs {counts} time')
    elif counts != 0 and counts > 1:
        print(f'{i} occurs {counts} times')
