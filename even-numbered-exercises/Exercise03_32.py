x0 = float(input("Enter the x-coordinate for Point p0: "))
y0 = float(input("Enter the y-coordinate for Point p0: "))
x1 = float(input("Enter the x-coordinate for Point p1: "))
y1 = float(input("Enter the y-coordinate for Point p1: "))
x2 = float(input("Enter the x-coordinate for Point p2: "))
y2 = float(input("Enter the y-coordinate for Point p2: "))

status = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    
if status <= 0.0000000001 and \
        ((x0 <= x2 and x2 <= x1) or (x0 >= x2 and x2 >= x1)):
    print("(" + str(x2) + ", " + str(y2) + ") is on the line segment from"
        + " (" + str(x0) + ", " + str(y0) + ") to " + "(" + 
        str(x1) + ", " + str(y1) + ")")
else: 
    print("(" + str(x2) + ", " + str(y2) + ") is not on the line segment from"
        + " (" + str(x0) + ", " + str(y0) + ") to " + "(" 
        + str(x1) + ", " + str(y1) + ")")
