x1 = float(input("Enter the x-coordinate for point1: "))
y1 = float(input("Enter the y-coordinate for point1: "))
x2 = float(input("Enter the x-coordinate for point2: "))
y2 = float(input("Enter the y-coordinate for point2: "))

m = (y2 - y1) / (x2 - x1);
b = y1 - m * x1;
    
print("The line equation for two points (", x1, ",",
    y1, ") and (", x2, ",", y2, ") is", "y =", end = ' ')
  
if m == -1:
    print("-x")
elif m == 1:
    print("x")
else: 
    print(m, end = '')
    print("x", end = ' ')

if b > 0:
    print("+", b)
elif b < 0:
    print("-", (-1 * b))
else: # b is 0
    print()