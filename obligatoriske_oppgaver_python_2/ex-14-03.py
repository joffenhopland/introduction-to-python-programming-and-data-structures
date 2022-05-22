import re

document = "/Users/joffenhopland/Library/Mobile Documents/com~apple~CloudDocs/Documents/Datateknikk/Programmering/Examples from pybook/Presidents.txt"
input_file = open(document, "r")
dictionary = {}
for line in input_file:
    trimmed = re.sub(r"[^a-zA-Z0-9 ]+", '', line)
    word_list = trimmed.split(" ")

    for word in word_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

print(dictionary)
