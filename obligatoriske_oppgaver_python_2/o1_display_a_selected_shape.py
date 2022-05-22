from tkinter import *


class DisplayShape:
    def __init__(self):
        window = Tk()
        window.title("Display Shapes")

        var = StringVar()
        var.set("Rectangle")  # initial value
        comboBox = OptionMenu(
            window,
            var,
            "Rectangle",
            "Oval",
            "Arc",
            "Polygon",
            "Line",
            command=self.selection,
        ).pack(fill=BOTH)

        # Create a canvas to display shapes
        self.canvas = Canvas(window, width=400, height=200, bg="white")
        self.canvas.pack()

        window.mainloop()  # Create an event loop

    # Display selected shape
    def selection(self, selectedItem):
        self.canvas.delete("shape")
        if selectedItem == "Rectangle":
            self.canvas.create_rectangle(10, 10, 390, 190, tags="shape")
        elif selectedItem == "Oval":
            self.canvas.create_oval(10, 10, 390, 190, fill="red", tags="shape")
        elif selectedItem == "Arc":
            self.canvas.create_arc(
                10, 10, 390, 190, start=0, extent=90, width=8, fill="red", tags="shape"
            )
        elif selectedItem == "Polygon":
            self.canvas.create_polygon(10, 10, 390, 190, 30, 50, tags="shape")
        elif selectedItem == "Line":
            self.canvas.create_line(10, 10, 390, 190, fill="red", tags="shape")


DisplayShape()
