number = int(input("Enter an integer: "))

reversedNumber = 0
if number != 0:
    reversedNumber = 10 * reversedNumber + number % 10
    number = number // 10

if number != 0:
    reversedNumber = 10 * reversedNumber + number % 10
    number = number // 10

if number != 0:
    reversedNumber = 10 * reversedNumber + number % 10
    number = number // 10

if number != 0:
    reversedNumber = 10 * reversedNumber + number % 10
    number = number // 10
     

print("The reversed number is", reversedNumber)
