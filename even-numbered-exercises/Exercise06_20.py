import math

def main():
    x1 = float(input("Enter the x-coordinate of Point 1: "))
    y1 = float(input("Enter the y-coordinate of Point 1: "))
    x2 = float(input("Enter the x-coordinate of Point 2: "))
    y2 = float(input("Enter the y-coordinate of Point 2: "))
    x3 = float(input("Enter the x-coordinate of Point 3: "))
    y3 = float(input("Enter the y-coordinate of Point 3: "))
     
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)
    
    A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
    B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
    C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

    print("The three angles are", round(A, 2), round(B, 2), round(C, 2))

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

main()
