def binaryToDecimal(binaryString):
    value = ord(binaryString[0]) - ord('0')
    for i in range(1, len(binaryString)):
        value = value * 2 + ord(binaryString[i]) - ord('0')
    
    return value
        
def main():
    binaryString = (input("Enter a binary number string: "))
    print(f"The decimal value is {binaryToDecimal(binaryString)}")
                
main()