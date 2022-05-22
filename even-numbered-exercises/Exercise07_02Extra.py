import math

def main():
    s = input("Enter the coordinates of six points separated by spaces: ")
    items = s.split() # Extract items from the string
    lst = [float(x) for x in items] # Convert items to numbers
    
    x = lst[0 : len(lst) : 2]
    y = lst[1 : len(lst) : 2]
    
    total = 0
    for i in range(1, len(x) - 1):
        total += getArea(x[0], y[0], x[i], y[i], x[i + 1], y[i + 1])
    
    print("The total area is", total)
  
def getArea(x1, y1, x2, y2, x3, y3):
    s1 = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 -y2))
    s2 = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 -y3))
    s3 = math.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 -y2))
    
    s = (s1 + s2 + s3) / 2
    return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

main()
