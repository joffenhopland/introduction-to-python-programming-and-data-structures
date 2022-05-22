def main():
    s = input("Enter a string s: ")
    b = int(input("Enter an integer b: "))

    print("The hashCode for", s, "is", hashCode(s, b))
  
def hashCode(s, b):
    hashCode = 0
    for i in range(0, len(s)):
        hashCode = hashCode * b + ord(s[i])
    
    return hashCode

main()