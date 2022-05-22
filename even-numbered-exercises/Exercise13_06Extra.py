def main():
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r") 
    lst = []
    for line in infile:
        items = line.split()
        for e in items:
            lst.append(e)
    
    isSorted = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            print("The words are not sorted. The first two out-of-order words:", lst[i], lst[i + 1])
            isSorted = False
            break;
        
    if isSorted:
        print("The words are sorted")
    
main()