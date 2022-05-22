import random

# Obtain the random number 0 or 1
number = random.randint(0, 1)

# Prompt the user to enter a guess
print("Guess head or tail?")
guess = int(input("Enter 0 for head and 1 for tail: "))

# Check the guess
if guess == number:
    print("Correct guess")
elif number == 0:
    print("Sorry, it is a head")
else:
    print("Sorry, it is a tail")
