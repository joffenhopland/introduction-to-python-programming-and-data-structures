import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
    number1, number2 = number2, number1

answer = int(input(f"What is {number1} - {number2} ? "))

choice = random.randint(0, 2)
if number1 - number2 == answer:
    if choice == 0:
        print("Excellent!")
    elif choice == 1:
        print("Correct")
    else:
        print("Way to go!")
else:
    if choice == 0:
        print("Incorrect")
    elif choice == 1:
        print("Wrong")
    else:
        print("Not right")
