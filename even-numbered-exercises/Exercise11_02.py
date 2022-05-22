from tkinter import * # Import tkinter

class ComboBoxDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Set Colors") # Set title

        # Create a combo box to select a country
        var = StringVar()
        var.set("red") # initial value
        comboBox = OptionMenu(window, var, "red", "green", "blue", 
            "yellow", "purple", "orange",
            command = self.processSelection).pack(fill = BOTH)

        self.label = Label(window, text = "Programming is fun")
        self.label["fg"] = "red"
        self.label.pack()
        
        window.mainloop() # Create an event loop
        
    # Display image for selected country
    def processSelection(self, selectedItem):
        self.label["fg"] = selectedItem
            
ComboBoxDemo() # Create GUI 