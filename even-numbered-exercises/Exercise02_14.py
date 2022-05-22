# Enter three points for a triangle
x1 = float(input("Enter x-coordinate of Point 1 for a triangle: "))
y1 = float(input("Enter y-coordinate of Point 1 for a triangle: "))
x2 = float(input("Enter x-coordinate of Point 2 for a triangle: "))
y2 = float(input("Enter y-coordinate of Point 2 for a triangle: "))
x3 = float(input("Enter x-coordinate of Point 3 for a triangle: "))
y3 = float(input("Enter y-coordinate of Point 3 for a triangle: "))

# Compute the length of the three sides
side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
side2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
side3 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5

s = (side1 + side2 + side3) / 2;
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print("The area of the triangle is", area)
