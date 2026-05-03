# Import all classes and functions from tkinter module
from tkinter import *
# Create the main window
root = Tk()
# mention window size
root.geometry("500x500")
# Create a label widget with text
label = Label(root, text="Hello Rohit",fg="green",bg="black",font=("Times New Roman",20))
# Place the label on the window
label.pack()
# Run the application (event loop)
root.mainloop()