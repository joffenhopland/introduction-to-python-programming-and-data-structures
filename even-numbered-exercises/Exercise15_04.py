def main():
    print(format("i", "<4s"), format("m(i)", "<10s"))
    for i in range(1, 10 + 1):
        print(format(i, "<4d"), format(m(i), "<10.4f"))

def m(i):
    if i == 1:
        return 1
    else:
        return m(i - 1) + 1.0 / i

main()
