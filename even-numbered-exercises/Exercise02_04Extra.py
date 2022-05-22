x1 = float(input("Enter the x-coordinate for point1: "))
y1 = float(input("Enter the y-coordinate for point1: "))
x2 = float(input("Enter the x-coordinate for point2: "))
y2 = float(input("Enter the y-coordinate for point2: "))
slope = (x1 - x2) / (y1 - y2)
print("The slope for the line that connects two points (",
    x1, ",", y1, ") and (", x2, ",", y2, ") is", slope)