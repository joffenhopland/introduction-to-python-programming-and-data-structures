def main():
    s = input("Enter the weights for each item: ")
    w = [float(x) for x in s.split()]
    
    weightLimit = float(input("Enter the weight limit for the bag: "))
    
    print("The maximum weight of the items placed in the bag is",
        m(len(w) - 1, weightLimit, w))
  
def m(i, weightLimit, w):
    if i == -1 or weightLimit <= 0:
        return 0
    elif w[i] > weightLimit:
        return m(i - 1, weightLimit, w)
    else:
      return max(m(i - 1, weightLimit, w), 
          w[i] + m(i - 1, weightLimit - w[i], w))
      
main()