# define main method
def main():

    # prompt the user to enter genome string
    print("Enter a genome string: ")
    string = input()

    # declare all the required variables
    i = 0
    found = 0
    start = -1

    # find the length of the string
    num = len(string)
    for i in range(num-2):

        # find the substring of genome string
        triplet = string[i:i+3]

        # compare the substring with following strings
        if triplet == "ATG":
            start = i+3
        elif triplet == "TAG" or triplet == "TAA" or triplet == "TGA" and start != -1:
            gene = string[start:i]
            if len(gene) % 3 == 0:
                found = 1

                # print the substring
                print(gene)
                start = -1
    # check if there is no gene string
    if found == 0:
        print("no gene is found")


main()
