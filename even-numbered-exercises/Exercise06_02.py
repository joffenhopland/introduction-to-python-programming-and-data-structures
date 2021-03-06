def main():
    value = int(input("Enter an integer: "))

    print("The sum of digits for", value, "is", sumDigits(value))

def sumDigits(n):
    temp = abs(n)
    sum = 0

    while temp != 0:
        remainder = temp % 10
        sum += remainder
        temp = temp // 10

    return sum

main()
