import turtle

radius = float(input("Enter radius: "))

turtle.penup()
turtle.goto(-radius, 0)
turtle.pendown()
turtle.circle(radius) 

turtle.penup()
turtle.goto(-radius, -2 * radius)
turtle.pendown()
turtle.circle(radius) 

turtle.penup()
turtle.goto(radius, 0)
turtle.pendown()
turtle.circle(radius) 

turtle.penup()
turtle.goto(radius, -2 * radius)
turtle.pendown()
turtle.circle(radius) 

turtle.done()
