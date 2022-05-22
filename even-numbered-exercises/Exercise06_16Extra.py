def main():
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    
    print("The P(n, k) is", getNumberOfPermutations(n, k))

def getNumberOfPermutations(n, k):
    result = 1
    
    for i in range(n - k + 1, n + 1):
        result = result * i
    
    return result;

main()