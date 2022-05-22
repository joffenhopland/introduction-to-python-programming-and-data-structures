def main():
    # Prompt the user to enter a string
    s = input("Enter a binary number string: ")
    print("The decimal value is", binaryToDecimal(s))

def binaryToDecimal(binaryString):
    value = ord(binaryString[0]) - ord('0')
    for i in range(1, len(binaryString)):
        value = value * 2 + ord(binaryString[i]) - ord('0')

    return value

main()