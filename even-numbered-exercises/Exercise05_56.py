s = input("Enter a string: ")

count = 0
for ch in s:
  if ch.isupper():
    count += 1
    
print("The number of uppercase letter in" , s, "is", count)
