def main():
    f1 = input("Enter a source filename: ").strip()
    f2 = input("Enter a target filename: ").strip()

    # Open files for input 
    inputFile = open(f1, "r")
    
    s = inputFile.read() # Read all from the file
    
    newS = ""
    
    for i in range(len(s)):
        newS += chr(ord(s[i]) + 5)

    inputFile.close()  # Close the input file
    outputFile = open(f1, "w")
    
    print(newS, file = outputFile, end = "") # Write to the file
    print("Done") 

    outputFile.close() # Close the output file

main()
