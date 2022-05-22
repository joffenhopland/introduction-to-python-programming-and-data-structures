def main():
    # Prompt the user to enter a file
    file1 = input("Enter a filename: ").strip()
    input_file1 = open(file1, "r")  # Open the file
    text1 = input_file1.read()  # Read all from the file to string
    set1 = process_text(text1)
    input_file1.close()

    # Prompt the user to enter another file
    file2 = input("Enter a filename: ").strip()
    input_file2 = open(file2, "r")  # Open the file
    text2 = input_file2.read()  # Read all from the file to string
    set2 = process_text(text2)
    input_file2.close()

    display(set1, set2)


def process_text(text):
    text = replace_punctuation(text.lower())
    words = text.split()  # list
    new_set = set(words)  # set
    return new_set


def replace_punctuation(text):
    for ch in text:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            text = text.replace(ch, "")
    return text


def display(set1, set2):

    # Count unique words
    print()
    unique_word_count1 = len(set1)
    print(f"Number of unique words in file 1: {unique_word_count1}")
    unique_word_count2 = len(set2)
    print(f"Number of unique words in file 2: {unique_word_count2}")
    print()

    # Display unique words
    print(f"Unique words in file 1: {set1}")
    print()
    print(f"Unique words in file 2: {set2}")
    print()

    # Unique words in both set1 and set2 (set intersection)
    set3 = set1 & set2
    print(set3)
    print()

    # Unique words in set1 that are not in set 2 (Set difference)
    set3 = set1 - set2
    print(set3)
    print()

    # Unique words in set2 that are not in set 1 (Set difference)
    set3 = set2 - set1
    print(set3)
    print()

    # Unique words in either set1 or set2, except for words in both (Set exclusive)
    set3 = set1 ^ set2
    print(set3)


main()  # Call the main function
