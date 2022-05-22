import urllib.request
import ssl


def main():
    url = input("Enter an URL for a file: ").strip()
    context = ssl._create_unverified_context()
    inputFile = urllib.request.urlopen(url, context=context)  # Open a URL
    s = inputFile.read().decode()  # Read the content as string
    print(s)

    counts = countLetters(s.lower())

    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(
                chr(ord("a") + i)
                + " appears "
                + str(counts[i])
                + (" time" if counts[i] == 1 else " times")
            )


# Count each letter in the string
def countLetters(s):
    counts = 26 * [0]  # Create and initialize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord("a")] += 1
    return counts


main()  # Call the main function
