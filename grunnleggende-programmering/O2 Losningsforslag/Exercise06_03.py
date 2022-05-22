def main():
    number = int(input("Enter a positive integer: "))
    
    if isPalindrome(number):
        print(number, "is a palindrome")
    else:
        print(number, "is not a palindrome")

# Return true if number is a palindrome
def isPalindrome(number):
    return number == reverse(number)

# Return the reversal of an integer, i.e. reverse(456) returns 654
def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10

    return result

main()
