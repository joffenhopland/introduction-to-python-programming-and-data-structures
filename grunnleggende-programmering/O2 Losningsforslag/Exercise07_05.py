def main():
    s = input("Enter the numbers: ") 
    items = s.split() # Extracts items from the string
    list1 = [int(x) for x in items] # Convert items to numbers

    list2 = []

    for number in list1:
        if not (number in list2):
            list2.append(number)

    print("The number of distinct numbers is", len(list2))
    print("The distinct numbers are: ", end = '')
    
    for number in list2:
        print(number, end = ' ')

main()
