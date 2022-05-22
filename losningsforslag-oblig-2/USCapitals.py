def main():
    fileInput = open("USCapitals.txt").read().split("\n")
    usDict = {}

    for x in fileInput:
        data = x.split(", ")
        usDict[data[0]] = data[1]
    searchKey = True
    while searchKey:
        try:
            searchKey = input("Enter state name: ")
            print(usDict[searchKey])
        except:
            print("State does not exist")
      
main()