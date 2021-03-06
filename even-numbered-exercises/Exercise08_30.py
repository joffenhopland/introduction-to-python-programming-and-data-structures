def main():
    a = float(input("Enter a00: "))
    b = float(input("Enter a01: "))
    c = float(input("Enter a10: "))
    d = float(input("Enter a11: "))
    e = float(input("Enter b0: "))
    f = float(input("Enter b1: "))
    A = [[a, b], [c, d]]
    B = [e, f]
    
    result = linearEquation(A, B)
    
    if result == None:
        print("The equation has no solution")
    else:
        print("x is", result[0], "and y is", result[1])

def linearEquation(a, b):
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    
    if determinant == 0:
        return None
    else:
        result = []
        x = (b[0] * a[1][1] - b[1] * a[0][1]) / determinant
        y = (b[1] * a[0][0] - b[0] * a[1][0]) / determinant
        result.append(x)
        result.append(y)
        return result

main()
