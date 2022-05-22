numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))

if numerator < denominator:
    print(f"{numerator} / {denominator} is a proper function")
elif numerator % denominator == 0:
    print(f"{numerator} / {denominator} is an improper function and it can be reduced to {numerator // denominator}")
else:
    print(f"{numerator} / {denominator} is an improper function and the mixed fraction is {numerator // denominator} + {numerator % denominator} / {denominator}")
