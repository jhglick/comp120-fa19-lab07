# File: welcome_message.py
# Author: Dr. Glick, COMP 120
# Date: October 15, 2019
# Description: Simple GUI to display a message.

import tkinter as tk
from tkinter import ttk

class WelcomeMessage:

    def __init__(self):
        # Create main window
        self.window = tk.Tk()
        self.window.geometry("500x200")
        self.window.title("Welcome message")
        self.DEFAULT_GREETING_STRING = "            "
        
        # Add name label
        self.name_label = tk.Label(self.window, bg = 'red', text = "Name")
        self.name_label.grid(row = 1, column = 1, sticky = "W", padx = 10, pady = (10, 2))
        # sticky = "W" forces the widget to be placed against the west boundary of the its cell.
        # padx = 10 puts 10 pixels on both sides of the label but inside of its cell.
        # pady = (10, 2) puts 10 pixels above and 2 below of the label but inside of its cell.

        # Add name field
        self.name = tk.Entry(self.window, bg = 'yellow', width = 20)
        self.name.grid(row = 2, column = 1, columnspan = 2, sticky = "NW", 
                                padx = 10, pady = (2, 10))
        # columnspan = 2 makes the widget span columns 1 and 2.
        # sticky = "NW" puts the widget in the northwest corner of its cell.

        # Add reset button
        self.reset_button = tk.Button(self.window, bg = 'green', 
                                        text = "Reset", command=self.reset_name_field)
        self.reset_button.grid(row = 2, column = 3, padx = 10, pady = 10)

        # Add display greeting button
        self.display_greeting_button = tk.Button(self.window, bg = 'yellow',  text = "Display greeting", 
                                command=self.display_greeting)
        self.display_greeting_button.grid(row = 3, column = 1, sticky="W", padx = 10, pady = 10)

        # Add greeting field
        self.greeting_string = tk.StringVar()  # A special string variable that will be associated
                                            # with the greeting label.  Whenever this variable changes
                                            # the label text changes.
        self.greeting_string.set(self.DEFAULT_GREETING_STRING)
        self.greeting = tk.Label(self.window, bg = 'pink', textvariable = self.greeting_string, 
                                    borderwidth = 2)
        self.greeting.grid(row = 3, column = 2, columnspan = 2, sticky="W", padx = 10, pady = 10)

        # Add quit button
        self.quit_button = tk.Button(self.window, bg = 'green', 
                                        text = "Quit", command=self.quit)
        self.quit_button.grid(row = 3, column = 3, padx = 10, pady = 10)


        # Extra space is divided among all of the rows, 
        # so they should be evenly spaced outl
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_rowconfigure(3, weight=1)

        # Extra space is divided among all of the columns, 
        # so they should be evenly spaced outl
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_columnconfigure(3, weight=1)


    def display_greeting(self):
        """ Change the text assigned to the displayed greeting.  """
        self.greeting_string.set("Hello, %s" % self.name.get())
        self.name_label['text'] = "NAME"  # Shows how to change the text in a label using
                                          # this 'dictionary' syntax.

    def reset_name_field(self):
        """ Reset to empty the text entry widget """
        self.name.delete(0, 'end') # this deletes the characters from index 0 to the end
        self.greeting_string.set(self.DEFAULT_GREETING_STRING)

    def quit(self):
        """ Reset to empty the text entry widget """
        self.window.destroy()

def main():
    # Create the GUI program
    program = WelcomeMessage()

    # Start the GUI event loop
    program.window.mainloop()

if __name__ == "__main__":
    main()