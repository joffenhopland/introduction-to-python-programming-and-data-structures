letter = input("Enter a letter: ")

if letter.upper() == 'A' or letter.upper() == 'E' or \
    letter.upper() == 'I' or letter.upper() == 'O' or \
    letter.upper() == 'U':
    print(letter, "is a vowel")
elif letter.isalpha():
    print(letter, "is a consonant")
else:
    print(letter, "is an invalid input")
