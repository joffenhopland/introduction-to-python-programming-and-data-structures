import os.path
import datetime
      
def main():
    dt = datetime.datetime.now()
    s = str(dt).replace(' ', '_').replace('.', '_').replace(":", '_')
    
    filename = input("Enter a file name: ")
     
    # Test if file exists
    if os.path.isfile(filename):
        os.rename(filename, filename + s)
        print("file", filename, "has been renamed to", filename + s)
    else:
        print("The file does not exist")
    
main()