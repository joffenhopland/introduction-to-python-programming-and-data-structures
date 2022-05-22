def main():
    s = input("Enter list1: ");
    items = s.split() # Extract items from the string
    lst1 = [int(x) for x in items] # Convert items to numbers
    
    s = input("Enter list1: ");
    items = s.split() # Extract items from the string
    lst2 = [int(x) for x in items] # Convert items to numbers
    
    lst = getCommonElements(lst1, lst2)
    if len(lst) == 0:
        print("list1 and list2 have no common elements")
    else:
        print("The common elements are", lst)
        
def getCommonElements(lst1, lst2):
    lst = []
    for e in lst1:
        if e in lst2:
            lst.append(e)
            
    return lst

main()