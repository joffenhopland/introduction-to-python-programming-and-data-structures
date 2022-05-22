from tkinter import *
from tkinter.filedialog import askopenfilename
import urllib.request
import ssl


def showResult():
    url_to_read = url.get()
    context = ssl._create_unverified_context()
    inputFile = urllib.request.urlopen(
        url_to_read, context=context)  # Open a URL
    s = inputFile.read().decode()  # Read the content as string
    print(s)

    counts = countLetters(s.lower())

    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            text.insert(END, chr(ord('a') + i) + " appears " + str(counts[i])
                        + (" time\n" if counts[i] == 1 else " times\n"))


# Count each letter in the string
def countLetters(s):
    counts = 26 * [0]  # Create and initialize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord("a")] += 1
    return counts


window = Tk()  # Create a window
window.title("Occurrence of Letters")  # Set title

frame1 = Frame(window)  # Hold four labels for displaying cards
frame1.pack()

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=40, height=10, wrap=WORD,
            yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)

frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Enter a url: ").pack(side=LEFT)
url = StringVar()
Entry(frame2, width=20, textvariable=url).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
