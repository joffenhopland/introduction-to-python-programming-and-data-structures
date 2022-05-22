value = int(input("Enter a decimal number between 0 and 15: "))
s = ""

temp = value
s = str(temp % 2) + s
temp = temp // 2

s = str(temp % 2) + s
temp = temp // 2

s = str(temp % 2) + s
temp = temp // 2

s = str(temp % 2) + s
  
print("The binary number for", value, "is", s)