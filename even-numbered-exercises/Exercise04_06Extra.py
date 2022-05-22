s = input("Enter a four-digit binary string: ")   
if len(s) != 4:
    print("Please enter exactly four binary digits")
else:
    value = 0
    value += ord(s[3]) - ord('0')
    value += (ord(s[2]) - ord('0')) * 2
    value += (ord(s[1]) - ord('0')) * 2 * 2
    value += (ord(s[0]) - ord('0')) * 2 * 2 * 2    
    print("The decimal number for", s, "is", value)