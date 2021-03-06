import turtle

x1 = float(input("Enter r1's center x-coordinate: "))
y1 = float(input("Enter r1's center y-coordinate: "))
w1 = float(input("Enter r1's width: "))
h1 = float(input("Enter r1's height: "))

x2 = float(input("Enter r2's center x-coordinate: "))
y2 = float(input("Enter r2's center y-coordinate: "))
w2 = float(input("Enter r2's width: "))
h2 = float(input("Enter r2's height: "))

# Draw rectangle 1
turtle.penup()
turtle.goto(x1 - w1 / 2, y1 - h1 / 2)
turtle.pendown()
turtle.goto(x1 + w1 / 2, y1 - h1 / 2)
turtle.goto(x1 + w1 / 2, y1 + h1 / 2)
turtle.goto(x1 - w1 / 2, y1 + h1 / 2)
turtle.goto(x1 - w1 / 2, y1 - h1 / 2)

# Draw rectangle 2
turtle.penup()
turtle.goto(x2 - w2 / 2, y2 - h2 / 2)
turtle.pendown()
turtle.goto(x2 + w2 / 2, y2 - h2 / 2)
turtle.goto(x2 + w2 / 2, y2 + h2 / 2)
turtle.goto(x2 - w2 / 2, y2 + h2 / 2)
turtle.goto(x2 - w2 / 2, y2 - h2 / 2)

xDistance = x1 - x2 if x1 - x2 >= 0 else x2 - x1
yDistance = y1 - y2 if y1 - y2 >= 0 else y2 - y1

turtle.penup()
turtle.goto(x1, y1 - h1)
turtle.pendown()
    
if xDistance <= (w1 - w2) / 2 and yDistance <= (h1 - h2) / 2:
    turtle.write("r2 is inside r1")
elif xDistance <= (w1 + w2) / 2 and yDistance <= (h1 + h2) / 2:
    turtle.write("r2 overlaps r1")
else:
    turtle.write("r2 does not overlap r1")
    
turtle.done()
