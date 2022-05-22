import math

def main():
    numberOfSides = int(input("Enter the number of sides: "))
    side = float(input("Enter the side: "))
    
    print("The area of the polygon is", area(numberOfSides, side))
  
def area(n, side):
    return n * side * side / math.tan(math.pi / n) / 4

main()
