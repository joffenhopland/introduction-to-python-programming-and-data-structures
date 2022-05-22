
def main():
    entry = input("Enter some integers: ")
    lst = list(map(float, entry.split()))
    ordered(lst)


def ordered(lst, ord="ascending"):
    sorted_lst = sorted(lst)
    if ord == "ascending":
        if lst == sorted_lst:
            print("The numbers in the list are in ascending order")
        else:
            print("The numbers in the list are NOT in ascending order")
    elif ord == "descending":
        sorted_lst.reverse()
        if lst == sorted_lst:
            print("The numbers in the list are in descending order")
        else:
            print("The numbers in the list are NOT in descending order")
    else:
        print("Plese choose 'ascending' or 'descending as the order'")


main()
