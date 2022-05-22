import os
from tkinter import *

occurrences = 0
number_of_dir = 0
number_of_files = 0


def main():
    file_path = dir_file_input.get().strip()
    word = word_input.get().strip()

    global occurrences
    global number_of_dir
    global number_of_files

    occurrences = 0
    number_of_dir = 0
    number_of_files = 0

    text_start.delete(1.0, "end")
    text_start.insert('end', "Search start.")
    text_dotted_start.delete(1.0, "end")
    text_dotted_start.insert('end', "-------------------------------------")
    text_path.delete(1.0, "end")
    text_number_of_dir.delete(1.0, "end")
    text_number_of_files.delete(1.0, "end")
    text_occurrences.delete(1.0, "end")
    text_dotted_end.delete(1.0, "end")
    text_dotted_end.insert('end', "-------------------------------------")
    text_end.delete(1.0, "end")
    text_end.insert('end', "Search end.")

    try:
        input_path(file_path, word)
    except:
        print("Nothing")


def input_path(file_path, word):
    global number_of_dir
    try:
        if not os.path.isfile(file_path):
            files_list = os.listdir(file_path)  # All files and subdirectories
            # Number of files in directory that are being searched
            number_of_dir += 1
            text_number_of_dir.delete(
                1.0, "end")
            text_number_of_dir.insert(
                "end", f"Searched: {number_of_dir} directories")
            for file in files_list:
                input_path(file_path + '/' + file, word)  # Recursive call
        else:  # Base case
            findWord(file_path, word)
    except:
        text_path.delete(1.0, "end")
        text_path.insert(
            "end", "File or directory does not exist")


def findWord(file, word):
    global number_of_files
    global occurrences
    try:
        input_file = open(file, "r")
        number_of_files += 1
        text_number_of_files.delete(
            1.0, "end")
        text_number_of_files.insert(
            "end", f"Searched: {number_of_files} files")
        for line in input_file:
            if line.find(word) > -1:
                print(file + ": " + line)
                text_path.insert('end', f"{file}: {line}")
                occurrences += 1
        text_occurrences.delete(1.0, "end")
        if occurrences == 0:
            text_occurrences.insert(
                'end', f'{word}, does not exist.')
        else:
            text_occurrences.insert(
                'end', f"found {occurrences} occurrences of '{word}'.")
    except:
        print("No match")
    finally:
        input_file.close()


# UI SETUP

window = Tk()
window.title("Find word in files")
window.config(padx=10, pady=10, background="lightgrey")
window.minsize(800, 350)

# top frame

top_frame = Frame(window, background="lightgrey")
top_frame.pack(side=TOP, padx=10, pady=10)

dir_file_input = Entry(top_frame, width=40)
dir_file_input.insert(0, 'Directory or filename')
dir_file_input.pack(expand=True, fill=BOTH, side=LEFT, padx=10)

word_input = Entry(top_frame, width=20)
word_input.insert(0, 'Word')
word_input.pack(expand=True, fill=BOTH, side=LEFT, padx=20)

search_button = Button(top_frame, text='Search', width=10, command=main)
search_button.pack(expand=True, fill=BOTH, side=LEFT, padx=10)


# bottom frame

bottom_frame = Frame(window, background="lightgrey")
bottom_frame.pack(expand=True, fill=BOTH, side=BOTTOM, padx=10, pady=10)

text_start = Text(bottom_frame, width=100, height=1)
text_start.pack(fill=BOTH, side=TOP)

text_dotted_start = Text(bottom_frame, width=100, height=1)
text_dotted_start.pack(fill=BOTH)

text_path = Text(bottom_frame, width=100, height=30)
text_path.pack(expand=True, fill=BOTH)

# create a scrollbar widget and set its command to the text widget
scrollbar = Scrollbar(text_path, orient='vertical', command=text_path.yview)
scrollbar.pack(side=RIGHT)

#  communicate back to the scrollbar
text_path['yscrollcommand'] = scrollbar.set

text_dotted_end = Text(bottom_frame, width=100, height=1)
text_dotted_end.pack(fill=BOTH)

text_end = Text(bottom_frame, width=100, height=1)
text_end.pack(fill=BOTH)

text_number_of_dir = Text(bottom_frame, width=100, height=1)
text_number_of_dir.pack(fill=BOTH)

text_number_of_files = Text(bottom_frame, width=100, height=1)
text_number_of_files.pack(fill=BOTH)

text_occurrences = Text(bottom_frame, width=100, height=1)
text_occurrences.pack(fill=BOTH)


window.mainloop()
