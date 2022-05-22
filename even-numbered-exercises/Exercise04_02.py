import math

x1 = float(input("Enter point 1's latitude in degrees: "))
y1 = float(input("Enter point 1's longitude in degrees: "))
x2 = float(input("Enter point 2's latitude in degrees: "))
y2 = float(input("Enter point 2's longitude in degrees: "))

d = 6371.01 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
      math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * 
      math.cos(math.radians(y1 - y2)));

print("The distance between the two points is", d, "km")
