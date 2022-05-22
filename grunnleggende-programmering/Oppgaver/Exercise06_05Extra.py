def main():
    s = input("Enter a string: ")
    print("The new string is", title(s))
   
def title(s):
    sb = ""
    
    for i in range(0, len(s)):
        ch = s[i]
        if (i == 0 and ch.islower()) or (i > 0 and s[i - 1] == ' ' and ch.islower()): 
            sb += ch.upper()
        else:
            sb += ch
    
    return sb
    
main()