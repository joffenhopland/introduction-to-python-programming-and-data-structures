import turtle

x = float(input("Enter the x-coordinate for the center of the rectangle: "))
y = float(input("Enter the y-coordinate for the center of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

turtle.penup()
turtle.goto(x - width / 2, y - height / 2)
turtle.pendown()
turtle.goto(x + width / 2, y - height / 2)
turtle.goto(x + width / 2, y + height / 2)
turtle.goto(x - width / 2, y + height / 2)
turtle.goto(x - width / 2, y - height / 2)

turtle.hideturtle()

turtle.done()
