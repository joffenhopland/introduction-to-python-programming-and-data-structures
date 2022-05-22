import math

m = float(input("Enter the mass of the cart: "))
theta = float(input("Enter the ramp angle: "))
g = 9.8
F = m * g * math.sin(math.radians(theta))
print("The force to push the cart is", F, "Newtons")