import turtle
import math
from UsefulTurtleFunctions import drawLine

# Draw H shapes with the specified order
def displayHShape(order, center, length):
    if order >= 0:
        p1 = [center[0] - length / 2, center[1] + length / 2]
        p2 = [center[0] - length / 2, center[1] - length / 2]
        p3 = [center[0] + length / 2, center[1] + length / 2]
        p4 = [center[0] + length / 2, center[1] - length / 2]

        # Draw an H shape
        drawLine(center[0] - length / 2, center[1], 
            center[0] + length / 2, center[1])
        drawLine(p1[0], p1[1], p2[0], p2[1])
        drawLine(p3[0], p3[1], p4[0], p4[1])
        
        # Recursively display three H shape of a smaller order
        displayHShape(order - 1, p1, length / 2)
        displayHShape(order - 1, p2, length / 2)
        displayHShape(order - 1, p3, length / 2)
        displayHShape(order - 1, p4, length / 2)
  
def main():
    order = int(input("Enter an order: "))
    length = float(input("Enter the length of a side: "))
    displayHShape(order, [0, 0], length)

    turtle.done()

main()
