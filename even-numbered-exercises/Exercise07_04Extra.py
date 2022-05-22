def main():
    # Prompt the user to enter a string
    s = input("Enter a string: ")

    counts = count(s)

    for i in range(0, 10):
        if counts[i] > 0: 
            print("Digit", i, "occurs", counts[i], 
                "times" if counts[i] > 1 else "time")

def count(s):
    counts = 10 * [0]
    
    for i in range(0, len(s)):
        if s[i].isdigit():
            counts[int(s[i])] += 1

    return counts

main()