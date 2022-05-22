s = (input(f'Enter the integers between 1 and 100: '))
lst = list(map(int, s.split()))
counts = 1

for i in range(1, 101):
    n = lst.count(i)
    if n != 0 and n == 1:
        print(f'{i} occurs {n} time')
    elif n != 0 and n > 1:
        print(f'{i} occurs {n} times')
