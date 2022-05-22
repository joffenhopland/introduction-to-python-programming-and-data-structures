import random
import math

r = 100
PI = 3.14159
print("Three random points are")

angle = random.randint(0, 360)
x = r * math.cos(angle * math.pi / 180)
y = r * math.sin(angle * math.pi / 180)
print("(" + str(x) + ", " + str(y) + ")")

import turtle

turtle.penup() 
turtle.goto(0, -r)
turtle.pendown() 
turtle.circle(r)

turtle.penup() 
turtle.goto(x, y)
turtle.pendown()
turtle.dot(5, "red")

angle = random.randint(0, 360)
x = r * math.cos(angle * math.pi / 180)
y = r * math.sin(angle * math.pi / 180)
turtle.penup() 
turtle.goto(x, y)
turtle.pendown()
turtle.dot(5, "red")

angle = random.randint(0, 360)
x = r * math.cos(angle * math.pi / 180)
y = r * math.sin(angle * math.pi / 180)
turtle.penup() 
turtle.goto(x, y)
turtle.pendown()
turtle.dot(5, "red")

turtle.hideturtle()
turtle.done()