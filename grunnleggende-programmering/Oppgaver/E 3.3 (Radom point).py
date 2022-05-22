import random
import math
radius = 5
angle = random.random() * 2 * math.pi
x = radius * random.random() * math.cos(angle)
y = radius * math.sin(angle)
distance = math.pow(x * x + y * y, 0.5)
print(f"The point is {x} , {y} and its distance to the center is {distance}")
