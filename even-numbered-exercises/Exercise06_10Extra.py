def main():
    numberOfRows = int(input("Enter the number of rows: "))
    
    for i in range(0, numberOfRows + 1):
        for j in range(0, numberOfRows - i + 1):
            print("  ", end = "")
      
        for j in range(0, i + 1):
            print(format(c(i, j), "4d"), end = "")
      
        print()

def c(m, n):
    return factorial(m) // factorial(m - n) // factorial(n)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

main()