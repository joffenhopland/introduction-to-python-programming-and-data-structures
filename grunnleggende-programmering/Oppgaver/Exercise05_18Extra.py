s = input("Enter a string: ")
print("The vowels are ", end = "")
for ch in s:
    if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' \
          or ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print(ch, end = '')
