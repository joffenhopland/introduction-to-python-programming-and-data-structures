def main():
    A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]    
    A[0][0] = float(input("Enter a11: "))
    A[0][1] = float(input("Enter a12: "))
    A[0][2] = float(input("Enter a13: "))
    A[1][0] = float(input("Enter a21: "))
    A[1][1] = float(input("Enter a22: "))
    A[1][2] = float(input("Enter a23: "))
    A[2][0] = float(input("Enter a31: "))
    A[2][1] = float(input("Enter a32: "))
    A[2][2] = float(input("Enter a33: "))

    b = [0, 0, 0]
    b[0] = float(input("Enter b1: "))
    b[1] = float(input("Enter b2: "))
    b[2] = float(input("Enter b3: "))
    
    delta = deltaA(A)
    if delta == 0:
        print("No solution")
    else:
        x = ((A[1][1] * A[2][2] - A[1][2] * A[2][1]) * b[0] + 
             (A[0][2] * A[2][1] - A[0][1] * A[2][2]) * b[1] + 
             (A[0][1] * A[1][2] - A[0][2] * A[1][1]) * b[2]) / delta
        y = ((A[1][2] * A[2][0] - A[1][0] * A[2][2]) * b[0] +
             (A[0][0] * A[2][2] - A[0][2] * A[2][0]) * b[1] +
             (A[0][2] * A[1][0] - A[0][0] * A[1][2]) * b[2]) / delta
        z = ((A[1][0] * A[2][1] - A[1][1] * A[2][0]) * b[0] +
             (A[0][1] * A[2][0] - A[0][0] * A[2][1]) * b[1] +
             (A[0][0] * A[1][1] - A[0][1] * A[1][0]) * b[2]) / delta

        print("The solution is", x, y, z)
      
def deltaA(A):
    result = A[0][0] * A[1][1] * A[2][2] + \
        A[2][0] * A[0][1] * A[1][2] + A[0][2] * A[1][0] * A[2][1] - \
        A[0][2] * A[1][1] * A[2][0] - A[0][0] * A[1][2] * A[2][1] - \
        A[2][2] * A[1][0] * A[0][1]
      
    return result
 
main()