from tkinter import *
from tkinter.filedialog import askopenfilename


def showResult():
    while True:
        try:
            filenameforReading = filename.get()
            inputFile = open(filenameforReading, "r")
            break
        except IOError:
            print("File " + filenameforReading + " does not exist. Try again")

    counts = 26 * [0]  # Create and initialize counts
    for line in inputFile:
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts)

    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            text.insert(END, chr(ord('a') + i) + " appears " + str(counts[i])
                        + (" time\n" if counts[i] == 1 else " times\n"))

    inputFile.close()  # Close file

# Count each letter in the string


def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1


def openFile():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)


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

Label(frame2, text="Enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text="Browse", command=openFile).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
