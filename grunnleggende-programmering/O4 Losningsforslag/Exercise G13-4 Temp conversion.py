
import tkinter

class CelsiusGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame
        self.celsius_label = tkinter.Label(self.top_frame,
                              text = 'Enter the Celsius temperature:')
        self.celsius_entry = tkinter.Entry(self.top_frame, width = 10)

        # Pack the top frame widgets
        self.celsius_label.pack(side = 'left')
        self.celsius_entry.pack(side = 'left')

        # Create the widgets for the middle frame
        self.results_label = tkinter.Label(self.mid_frame,
                              text = 'Fahrenheit temperature: ')
                  
        # Create a blank label 
        self.fahr = tkinter.StringVar()
        self.fahrenheit_label = tkinter.Label(self.mid_frame, textvariable= self.fahr)

        # Pack the middle frame widgets
        self.results_label.pack(side = 'left')
        self.fahrenheit_label.pack(side = 'left')
                                                           
        # Create the two buttons in the bottom frame
        self.fahrenheit_button = tkinter.Button(self.bottom_frame,
                                  text = 'Convert to Fahrenheit',
                                  command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                            text = 'Quit',
                            command = self.main_window.destroy)

        # Pack the widgets in the bottom frame
        self.fahrenheit_button.pack(side='left')
        self.quit_button.pack(side='left')
                
        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def convert(self):
        # Get the values entered
        self.celsius = float(self.celsius_entry.get())

        # Calculate fahrenheit
        self.fahrenheit = 9.0 /5.0 * float(self.celsius) + 32

        # Update the fahrenheit_label
        self.fahr.set(self.fahrenheit)
        
# Create an instance of CelsiusGUI
if __name__ == '__main__':
    celsius = CelsiusGUI()