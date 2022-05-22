##
# Determine whether or not two strings are anagrams and report the result.
#
## Compute the frequency distribution for the characters in a string
# @param s the string to process
# @return a dictionary mapping each character to its count
def characterCounts(s):
    # Create a new, empty dictionary
    counts = {}
    # Update the count for each character in the string
    for ch in s:
        if ch in counts:
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1
    # Return the result
    return counts

# Determine if two strings entered by the user are anagrams
def main():
    # Read the strings from the user
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")

    # Get the character counts for each string
    counts1 = characterCounts(s1)
    counts2 = characterCounts(s2)
    # Display the result
    if counts1 == counts2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")    

main() # Call the main function