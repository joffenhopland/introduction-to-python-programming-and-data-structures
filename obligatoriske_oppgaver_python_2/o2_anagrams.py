def main():
    string1 = input("Enter a string: ")
    string2 = input("Enter another string: ")
    if test_anagrams(string1, string2):
        print(f"{string1} and {string2} are anagrams")
    else:
        print(f"{string1} and {string2} are NOT anagrams")


def test_anagrams(string1, string2):
    string1_count = {}
    for letter in string1.lower():
        if letter in string1_count:
            string1_count[letter] += 1  # Increase count for word
        else:
            string1_count[letter] = 1  # Add an item in the dictionary
    string2_count = {}
    for letter in string2.lower():
        if letter in string2_count:
            string2_count[letter] += 1  # Increase count for word
        else:
            string2_count[letter] = 1  # Add an item in the dictionary

    print(string1_count)
    print(string2_count)

    return string1_count == string2_count


main()
