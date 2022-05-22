# Struktur:
# 1. En evig while lokke rundt "det hele"
# 2. En meny med 5 valg
# 3. Faa tak i valg fra bruker
# 4. Generer to tall random, mellom 1 of 9\
# 5. Sjekk hvilken regneart, lag sporsmaal, spor bruker om svar
# 6. Sjekk om korrekt svar eller ikke, presenter resultat
# 7. Hvis valg 5, break ut av while

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
        answer = int(input("What is " + str(number1) +
                     " + " + str(number2) + "? "))
        if number1 + number2 == answer:
            print("Correct")
        else:
            print("Your answer is wrong. The correct answer is",
                  (number1 + number2))
    elif choice == 2:
        if number1 < number2:  # Swap number1 with number2
            number1, number2 = number2, number1
        answer = int(input("What is " + str(number1) +
                     " - " + str(number2) + "? "))
        if number1 - number2 == answer:
            print("Correct")
        else:
            print("Your answer is wrong. The correct answer is",
                  (number1 - number2))
    elif choice == 3:
        answer = int(input("What is " + str(number1) +
                     " * " + str(number2) + "? "))
        if number1 * number2 == answer:
            print("Correct")
        else:
            print("Your answer is wrong. The correct answer is",
                  (number1 * number2))
    elif choice == 4:
        number2 = random.randint(1, 9)
        answer = int(input("What is " + str(number1) +
                     " // " + str(number2) + "? "))
        if number1 // number2 == answer:
            print("Correct")
        else:
            print("Your answer is wrong. The correct answer is",
                  (number1 // number2))
    elif choice == 5:
        break
