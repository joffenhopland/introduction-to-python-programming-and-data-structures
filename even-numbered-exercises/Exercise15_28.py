import os

def main():
    path = input("Enter a directory or a file: ").strip()  
    s = input("Enter a string: ").strip()  
   
    # Display the size
    try:
        findinput(path, s)
    except:
        print("File or directory does not exist")

def findinput(path, word):
    try:
        if not os.path.isfile(path):
            list = os.listdir(path) # All files and subdirectories
            for i in range(len(list)):
                findinput(list[i], word) # Recursive call
        else: # Base case
          findWord(path, word)
    except:
        print("Let it go")

def findWord(file, word):
    try:
        inputFile = open(file, "r")
        for line in inputFile:
            if line.find(word) > -1:
                print(file + ": " + line)
    except:
        print("Let is go")
    finally:   
        inputFile.close()
    
main()
