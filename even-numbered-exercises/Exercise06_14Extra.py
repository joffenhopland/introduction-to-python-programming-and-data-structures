def main():
    s = input("Enter string s: ")
    s1 = input("Enter string s1: ")

    if isPrefix(s, s1):
        print(s1, "is a prefix of", s)
    else:
        print(s1, "is not a prefix of", s)

# Return true if s1 is a prefix of s 
def isPrefix(s, s1):
    if len(s1) > len(s):
        return False
  
    for i in range(0, len(s1)):
        if s[i] != s1[i]:
            return False
  
    return True

main()