def main():
    value = int(input("Enter an integer: "))
    print(f"The binary value is {decimalToBinary(value)}")
    
def decimalToBinary(value):
    binary = ""
    
    while value != 0:
        bit = value % 2
        binary = binary + str(bit)
        value = value // 2
        
    return binary

main()