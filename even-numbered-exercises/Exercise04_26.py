import sys

s = input("Enter two characters: ")

if s[0] == 'M':
    print("Mathematics ")
elif s[0] == 'C':
    print("Computer Science ")
elif s[1] == 'I':
    print("Information Technology ")
else:
    print("Input major code")
    sys.exit()

if s[1] == '1':
    print("Freshman")
elif s[1] == '2':
    print("Sophomore")
elif s[1] == '3':
    print("Junior")
elif s[1] == '4':
    print("Senior")
else:
    print("Input status code")
  