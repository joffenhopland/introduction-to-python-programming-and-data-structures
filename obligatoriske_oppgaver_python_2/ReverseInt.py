from tkinter import *


def main():
    integer = int(integer_input.get())
    result.delete(0, 'end')
    reverseInteger(integer)


def reverseInteger(value):
    if value != 0:
        reverse_nums = value % 10
        result.insert("end", reverse_nums)
        value //= 10
        reverseInteger(value)


window = Tk()
window.title("Reverse Integer")
window.config(padx=10, pady=10)
window.minsize(500, 100)

integer_input = Entry(width=40)
integer_input.insert(0, 'Enter an integer')
integer_input.grid(row=0, column=0)

search_button = Button(text='Reverse', width=10, command=main)
search_button.grid(row=0, column=1)

result = Entry(width=50)
result.grid(row=1, column=0, columnspan=3)

window.mainloop()
