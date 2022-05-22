def main():
    # Prompt the user to enter a string
    value = int(input("Enter an integer: "))
    print("The binary value is", decimalToBinary(value))

def decimalToBinary(value):
    buffer = ""

    while value != 0:
        bit = value % 2
        buffer = buffer + str(bit)
        value = value // 2

    return buffer

main()