import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter import *


def red(value=1):
    selection = "You selected the option 1"
    label.config(text = selection)
    label.configure(background='red')
def green(value=2):
    selection = "You selected the option 2"
    label.config(text = selection)
    label.configure(background='green')
def blue(value=3):
    selection = "You selected the option 3"
    label.config(text = selection)
    label.configure(background='blue')

root = tk.Tk()
var = IntVar()
Label(root, text='tk', justify = LEFT, padx=20).pack()
Radiobutton(root, text='Red', variable=var, value=1, command=red).pack(anchor=W)
Radiobutton(root, text='Green', variable=var, value=2, command=green).pack(anchor=W)
Radiobutton(root, text='Blue', variable=var, value=3, command=blue).pack(anchor=W)


label = Label(root, text = "No selection", background='purple')
label.pack()

root.mainloop()