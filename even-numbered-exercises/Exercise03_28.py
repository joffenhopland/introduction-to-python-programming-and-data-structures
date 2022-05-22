x1 = float(input("Enter r1's center x-coordinate: "))
y1 = float(input("Enter r1's center y-coordinate: "))
w1 = float(input("Enter r1's width: "))
h1 = float(input("Enter r1's height: "))

x2 = float(input("Enter r2's center x-coordinate: "))
y2 = float(input("Enter r2's center y-coordinate: "))
w2 = float(input("Enter r2's width: "))
h2 = float(input("Enter r2's height: "))

xDistance = x1 - x2 if x1 - x2 >= 0 else x2 - x1
yDistance = y1 - y2 if y1 - y2 >= 0 else y2 - y1
    
if xDistance <= (w1 - w2) / 2 and yDistance <= (h1 - h2) / 2:
    print("r2 is inside r1")
elif xDistance <= (w1 + w2) / 2 and yDistance <= (h1 + h2) / 2:
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")
