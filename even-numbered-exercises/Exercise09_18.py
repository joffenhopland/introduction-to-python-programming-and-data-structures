import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b * b - 4 * a * c
    
if discriminant < 0:
    r1 = complex(-b / (2 * a), math.sqrt(-discriminant) / (2 * a))
    r2 = complex(-b / (2 * a), math.sqrt(-discriminant) / (2 * a))
    print("The roots are", r1, "and", r2)
elif discriminant == 0:
    r1 = -b / (2 * a)
    print("The root is " + str(r1))
else:
    # (discriminant > 0)
    r1 = (-b + discriminant ** 0.5) / (2 * a)
    r2 = (-b - discriminant ** 0.5) / (2 * a)
    print("The roots are", r1, "and", r2)