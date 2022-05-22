from tkinter import *
from tkinter.ttk import Combobox

def main():
    n1 = int(first_number_entry.get())
    n2 = int(second_number_entry.get())

    n1_bin = bin(n1)[2:]
    n2_bin = bin(n2)[2:]

    first = int(n1_bin, 2)
    second = int(n2_bin, 2)

    your_answer = your_answer_entry.get()
    selected_item = combo_box.get()

    if selected_item == "AND":
        correct_answer_label.config(text=f'{first & second:08b}')
        correct_answer = f'{first & second:08b}'
        if your_answer == correct_answer:
            your_answer_entry.config({"background": "Green"})
        else:
            your_answer_entry.config({"background": "Red"})
    elif selected_item == "OR":
        correct_answer_label.config(text=f'{first | second:08b}')
        correct_answer = f'{first | second:08b}'
        if your_answer == correct_answer:
            your_answer_entry.config({"background": "Green"})
        else:
            your_answer_entry.config({"background": "Red"})
    elif selected_item == "XOR":
        correct_answer_label.config(text=f'{first ^ second:08b}')
        correct_answer = f'{first ^ second:08b}'
        if your_answer == correct_answer:
            your_answer_entry.config({"background": "Green"})
        else:
            your_answer_entry.config({"background": "Red"})
    elif selected_item == "OCOMP":
        correct_answer_label.config(text=f'{~first & 255:08b}')
        correct_answer = f'{~first & 255:08b}'
        if your_answer == correct_answer:
            your_answer_entry.config({"background": "Green"})
        else:
            your_answer_entry.config({"background": "Red"})
    elif selected_item == "SHIFTLEFT(1)":
        correct_answer_label.config(text=f'{first<<1 & 255:08b}')
        correct_answer = f'{first<<1 & 255:08b}'
        if your_answer == correct_answer:
            your_answer_entry.config({"background": "Green"})
        else:
            your_answer_entry.config({"background": "Red"})
    elif selected_item == "SHIFTRIGHT(1)":
        correct_answer_label.config(text=f'{first>>1:08b}')
        correct_answer = f'{first>>1:08b}'
        if your_answer == correct_answer:
            your_answer_entry.config({"background": "Green"})
        else:
            your_answer_entry.config({"background": "Red"})



def int_to_binary():
    n1 = int(first_number_entry.get())
    n2 = int(second_number_entry.get())

    n1_bin = bin(n1)[2:]
    n2_bin = bin(n2)[2:]

    first = int(n1_bin, 2)
    second = int(n2_bin, 2)

    first_bin_label.config(text=f'{first:08b}')
    second_bin_label.config(text=f'{second:08b}')



### GUI ###
window = Tk()
window.title("Bitwise operators")
window.config(padx=20, pady=20)

# Labels
first_number_label = Label(text="First number, range 0 - 255")
first_number_label.grid(row=0, column=0)
second_number_label = Label(text="Second number, range 0 - 255")
second_number_label.grid(row=1, column=0)
your_answer_label = Label(text="Your answer")
your_answer_label.grid(row=2, column=0)
correct_answer_label = Label(text="Correct answer")
correct_answer_label.grid(row=3, column=0)
first_bin_label = Label(text="Binary")
first_bin_label.grid(row=0, column=2)
second_bin_label = Label(text="Binary")
second_bin_label.grid(row=1, column=2)
correct_answer_label = Label(text="")
correct_answer_label.grid(row=3, column=2)
info_label = Label(
    text="Only first number for SHIFTRIGHT(1), SHIFTLEFT(1) and OCOMP")
info_label.grid(row=0, column=3)

# Entries
first_number_entry = Entry(width=8)
first_number_entry.grid(row=0, column=1)
second_number_entry = Entry(width=8)
second_number_entry.grid(row=1, column=1)
your_answer_entry = Entry(width=8)
your_answer_entry.grid(row=2, column=2)

# Combobox
var_init = StringVar()  # StringVar for OptionMenu item values
var_init.set("AND")  # initial value
combo_box = Combobox(window, values=("AND", "OR", "XOR", "OCOMP", "SHIFTLEFT(1)", "SHIFTRIGHT(1)"))
combo_box.grid(row=2, column=3)
combo_box.set("AND")

# Buttons
bin_button = Button(text="Convert input to binary", command=int_to_binary)
bin_button.grid(row=1, column=3)
check_button = Button(text="Check", command=main)
check_button.grid(row=2, column=4)


window.mainloop()