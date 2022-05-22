# While loop around everything
# Print the menu
# Ask user to enter a number 1, 2, 3, 4 or 5.
# Generate two random numbers, number1 and number2
# For subtraction, if number1 < number2, swap the numbers
# For a division such as number1 / number2, number2 is not zero.
# Ask user to give an answer to the equation.
# If it's correct, print correct. Otherwise, print wrong.
# Redisplay menu after test is finished
# Enter 5 to break out of loop


import random

while True:
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")

    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    choice = int(input("Enter a choice: "))

    if choice == 1:
        guess = int(input(f"What is {num1} + {num2}? "))
        answer = num1 + num2
        if guess == answer:
            print("Correct!")
            print()
        else:
            print(f"Your answer is wrong. The correct answer is {answer}")
            print()

    elif choice == 2:
        if num1 < num2:
            num1, num2 = num2, num1
        guess = int(input(f"What is {num1} - {num2}? "))
        answer = num1 - num2
        if guess == answer:
            print("Correct!")
            print()
        else:
            print(f"Your answer is wrong. The correct answer is {answer}")
            print()

    elif choice == 3:
        guess = int(input(f"What is {num1} * {num2}? "))
        answer = num1 * num2
        if guess == answer:
            print("Correct!")
            print()
        else:
            print(f"Your answer is wrong. The correct answer is {answer}")
            print()

    elif choice == 4:
        if num2 == 0:
            num1, num2 = num2, num1
        guess = float(input(
            f"What is {num1} / {num2}? (if your guess includes several decimals\nthen round up to two decimals): "))
        answer = round(num1 / num2, 2)
        if guess == answer:
            print("Correct!")
            print()
        else:
            print(f"Your answer is wrong. The correct answer is {answer}")
            print()
    elif choice == 5:
        break
