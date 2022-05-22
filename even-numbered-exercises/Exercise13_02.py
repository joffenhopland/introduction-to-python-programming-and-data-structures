def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()

    # Open files for input 
    inputFile = open(f1, "r")
    
    s = inputFile.read() # Read all from the file
    
    print(str(len(s)) + " characters") 
    print(str(len(s.split())) + " words") 
    print(str(len(s.split('\n'))) + " lines") 
    
    input.close() # Close the output file

main()
