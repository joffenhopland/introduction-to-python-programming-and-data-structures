def main():
    i = int(input("Enter i: "))
    print("m(" + str(i) + ") is " + str(m(i)))

def m(i):
    if i == 1:
        return 1.0 / 2
    else:
        return m(i - 1) + i * 1.0 / (i + 1)

main()
