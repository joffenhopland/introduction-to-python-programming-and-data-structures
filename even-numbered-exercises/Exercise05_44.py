decimal = int(input("Enter a decimal integer: "))
    
binaryString = ""
value = decimal

while value != 0:
    binaryString = str(value % 2) + binaryString
    value = value // 2

print(str(decimal) + "'s binary representation is " + binaryString)
