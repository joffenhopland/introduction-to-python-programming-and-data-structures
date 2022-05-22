import urllib.request

def main():
    inputFile = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
    s = input.read()

    print("The number of words in the file is " + str(len(s.split())))
main()
