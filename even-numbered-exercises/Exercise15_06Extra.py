def main():
    s = input("Enter integers for a list: ")
    lst = [int(x) for x in s.split()]
    
    cube(lst, 0, len(lst) - 1)
    
    for e in lst:
        print(e, end = ' ')
    print()

def cube(lst, low, high):
    if low <= high: # Base case
        lst[low] = lst[low] * lst[low] * lst[low]
        cube(lst, low + 1, high)
        
main()