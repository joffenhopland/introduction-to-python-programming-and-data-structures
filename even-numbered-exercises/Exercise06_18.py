import random

def main():
    n = int(input("Enter n: "))
    printMatrix(n)

def printMatrix(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(random.randint(0, 1), end = " ")

        print()
        
main()
