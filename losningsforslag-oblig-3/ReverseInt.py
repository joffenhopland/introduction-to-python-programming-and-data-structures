import tkinter as tk


class GUI:
    def __init__(self):
        window = tk.Tk()
        window.title("Reverse Integer")
        window.geometry("400x140")
        self.result = ""
        self.inpVar = tk.IntVar()

        inFrame = tk.Frame(window)
        intInput = tk.Entry(inFrame, textvariable=self.inpVar, width=40)
        revButton = tk.Button(inFrame, text="Reverse", width=10, command=self.buttonHandler)
        outFrame = tk.Frame(window)
        self.intOutput = tk.Text(outFrame, width=40, height=1)

        inFrame.pack(pady=20)
        intInput.grid(column=0, row=0)
        revButton.grid(column=1, row=0)
        outFrame.pack()
        self.intOutput.pack()

        window.mainloop()

    def buttonHandler(self):
        self.intOutput.delete(0.0, tk.END)
        self.reverseInteger(self.inpVar.get())
        self.intOutput.insert(tk.END, self.result)
        self.result = ""

    def reverseInteger(self, value):
        if value < 10:
            self.result += str(value)
        else:
            lastNumber = value % 10
            self.result += str(lastNumber)
            self.reverseInteger(value // 10)
    

GUI()