def dec2Hex(decimal):
    # Convert decimal to hex
    hex = ""
    
    while decimal != 0:
        hexValue = decimal % 16
      
        # Convert a decimal value to a hex digit 
        if 0 <= hexValue <= 9 and hexValue >= 0:
            hexChar = chr(hexValue + ord('0'))
        else: 
            hexChar = chr(hexValue - 10 + ord('A'))
      
        hex = hexChar + hex
        decimal = decimal // 16
    
    return hex

def main():
    value = int(input("Enter a decimal integer: "))
    print(dec2Hex(value))
    
main()