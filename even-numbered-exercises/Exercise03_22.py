# Enter a point with two double values
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

# Compute the distance
distance = (x * x +  y * y) ** 0.5
    
if distance <= 10:
    print("Point (" + str(x) + ", " + str(y) + ") is in the circle")
else:
    print("Point (" + str(x) + ", " + str(y) + ") is not in the circle")
