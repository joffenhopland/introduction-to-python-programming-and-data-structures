import math
u = float(input("Enter the coefficient of friction: "))
theta = float(input("Enter the angle: "))
g = 9.8
a = g * math.sin(math.radians(theta)) - u * math.cos(math.radians(theta))

if a <= 0:
    print("The brick does not move or move at a constant speed")
else:
    print("The brick accelerates at", a, "meters per square seconds")