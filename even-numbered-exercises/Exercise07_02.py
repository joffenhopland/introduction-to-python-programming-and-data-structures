def main():
    # Read numbers as a string from the console
    s = input("Enter numbers separated by spaces from one line: ") 
    items = s.split() # Extracts items from the string
    numbers = [int(x) for x in items ] # Convert items to numbers
    numbers.reverse()
    print("The reversed list is", end = ' ')
    for e in numbers:
        print(e, end = ' ')
    
main()
