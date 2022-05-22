s = input("Enter a string: ")

print("The reversed string is ", end = "")
for i in range(len(s) - 1, -1, -1):
    print(s[i], end = "")