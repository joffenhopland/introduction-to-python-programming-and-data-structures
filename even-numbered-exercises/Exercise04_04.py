import math

side = float(input("Enter the side: "))
# Compute the area
area = 6 * side * side / math.tan(math.pi / 6) / 4

print("The area of the hexagon is", area)
