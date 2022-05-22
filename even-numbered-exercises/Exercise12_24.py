class MyString(str):
    # Create a MyString
    def __init__(self, s = ""):
        self.s = s
        #super().__init__(s)

    # Return true if this string is equal to 
    # the string s case insensitive
    def equalsIgnoreCaseWith(self, s): 
        return self.s.upper() == s.upper()
  
def main():
    s1 = input("Enter string s1: ")
    s2 = input("Enter string s2: ")
    
    print(MyString(s1).equalsIgnoreCaseWith(s2))
  
main()