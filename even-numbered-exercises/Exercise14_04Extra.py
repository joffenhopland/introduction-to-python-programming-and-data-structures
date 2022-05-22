def main():
    s = input("Enter a text: ") # Read all from the file
    
    words = s.split()
    nonduplicateWords = set(words)
    words = list(nonduplicateWords)
    words.sort()
    
    for word in words:
        print(word, end = " ") 

main()
