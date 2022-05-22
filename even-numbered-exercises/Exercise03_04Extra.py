import random

# 1. Generate two random single-digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
  number1, number2 = number2, number1

# 3. Prompt the student to answer "what is number1 - number2?"
answer = int(input("What is " + str(number1) + " - " + str(number2) + "? "))

# 4. Grade the answer and display the result
choice = random.randint(0, 2)
if number1 - number2 == answer:
    if choice == 0:
        print("excellent")
    elif choice == 1:
        print("correct")
    else:
        print("way to go")
else:
    if choice == 0:
        print("incorrect")
    elif choice == 1:
        print("wrong")
    else:
        print("not right")
