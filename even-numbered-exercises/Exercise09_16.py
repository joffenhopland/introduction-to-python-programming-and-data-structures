import Rational

def getFraction(decimal):
    items = decimal.split(".")
    if len(items) <= 1:
        return decimal
    else:
        return Rational.Rational(int(items[0] + items[1]), 10 ** len(items[1]))
    
decimal = input("Enter a decimal number: ")
print("The fraction number is", getFraction(decimal))