import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getDiscriminant(self):
        return self.__b * self.__b - 4 * self.__a * self.__c

    def getRoot1(self):
        return (-self.__b + math.sqrt(self.getDiscriminant())) / (2 * self.__a)

    def getRoot2(self):
        return (-self.__b - math.sqrt(self.getDiscriminant())) / (2 * self.__a)

def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    equation = QuadraticEquation(a, b, c)
    discriminant = equation.getDiscriminant()

    if discriminant < 0:
        print("The equation has no roots")
    elif discriminant == 0:
        print("The root is", equation.getRoot1())
    else: # (discriminant >= 0)
        print("The roots are", equation.getRoot1(), "and", equation.getRoot2())
          
main()
