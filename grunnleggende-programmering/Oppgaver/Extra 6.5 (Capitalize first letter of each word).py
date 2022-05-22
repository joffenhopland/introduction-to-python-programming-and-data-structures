def main():
    s = input("Enter a string: ")
    print(f"The new string is: {title(s)}")


def title(s):
    value = ""
    
    for i in range(0, len(s)):
        ch = s[i]
        if (i == 0 and ch.islower()) or (i > 0 and s[i - 1] == ' ' and ch.islower()):
            value += ch.upper()
        else:
            value += ch
            
    return value

main()