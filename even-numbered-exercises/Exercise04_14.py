import random
import math

r = 40
PI = 3.14159
print("Three random points are")

angle = random.randint(0, 360)
x = r * math.cos(angle * math.pi / 180)
y = r * math.sin(angle * math.pi / 180)
print("(" + str(x) + ", " + str(y) + ")")

angle = random.randint(0, 360)
x = r * math.cos(angle * math.pi / 180)
y = r * math.sin(angle * math.pi / 180)
print("(" + str(x) + ", " + str(y) + ")")

angle = random.randint(0, 360)
x = r * math.cos(angle * math.pi / 180)
y = r * math.sin(angle * math.pi / 180)
print("(" + str(x) + ", " + str(y) + ")")

