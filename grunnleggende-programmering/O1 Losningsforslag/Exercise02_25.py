#  Read a number
number = int(input("Enter an integer between 0 and 1000: "))

lastDigit = number % 10
remainingNumber = number // 10
secondLastDigit = remainingNumber % 10

remainingNumber = remainingNumber // 10
thirdLastDigit = remainingNumber % 10

# Obtain the sum of all digits
sum = lastDigit + secondLastDigit + thirdLastDigit

# Display results
print("The sum of all digits in", number, "is", sum)
