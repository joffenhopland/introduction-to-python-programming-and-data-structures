import random
while True:
    print("Main menu")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")
    choice = int(input("Enter a choice: "))
    
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    
    if choice == 1:
        answer = int(input("What is " + str(number1) + " + " + str(number2) + "? "))
        if number1 + number2 == answer:
            print("Correct")
        else:
            print("Your answer is wrong. The correct answer is", (number1 + number2))
    elif choice == 2:
        if number1 < number2: # Swap number1 with number2
            number1, number2 = number2, number1
        answer = int(input("What is " + str(number1) + " - " + str(number2) + "? "))
        if number1 - number2 == answer:
            print("Correct")
        else:
            print("Your answer is wrong. The correct answer is", (number1 - number2))
    elif choice == 3:
        answer = int(input("What is " + str(number1) + " * " + str(number2) + "? "))
        if number1 * number2 == answer:
            print("Correct")
        else:
            print("Your answer is wrong. The correct answer is", (number1 * number2))
    elif choice == 4:
        number2 = random.randint(1, 9)
        answer = int(input("What is " + str(number1) + " // " + str(number2) + "? "))
        if number1 // number2 == answer:
            print("Correct")
        else:
            print("Your answer is wrong. The correct answer is", (number1 // number2))
    elif choice == 5:
        break
