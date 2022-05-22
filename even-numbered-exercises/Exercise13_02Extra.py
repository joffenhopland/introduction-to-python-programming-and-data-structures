import urllib.request

names = []
    
def readNames():
    for i in range(0, 10):
        if i == 9:
            filename = "babynamesranking2010.txt"
        else:
            filename = "babynamesranking200" + str(i + 1) + ".txt"
      
        inputFile = urllib.request.urlopen(
            "https://liveexample.pearsoncmg.com/data/" + filename)
        for line in inputFile:
            items = line.split()
            names.append(items[1].decode())
            names.append(items[3].decode())
        
    return names

def writeNames(names):   
    outputFile = open("test.txt", "w") 
    for i in range(len(names)):
        if (i + 1) % 10 != 0:
            outputFile.write(names[i] + " ")
        else:
            outputFile.write(names[i] + "\n")

def main():
    names = readNames()
    names.sort()
    writeNames(names)
    print("File written")
        
main()