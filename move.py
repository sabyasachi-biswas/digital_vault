from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
import tkinter.filedialog as filedialog
import filetype_module
import sqlite3
import os
import shutil

file = ""
filename = ""

def openfile():
    file = filedialog.askopenfilename()
    print(file)
    filename = filetype_module.filename(file)
    print(filename)

def movefile():
    file = filedialog.askopenfilename()
    print(file)
    filename = filetype_module.filename(file)
    print(filename)
    dest = filedialog.askdirectory()
    print(os.path.join(dest, filename))
    shutil.move(file,os.path.join(dest, filename))

root = Tk()
root.geometry("500x500")
btn1 = Button(root,text="Open",command = openfile)
btn1.pack()
btn2 = Button(root,text="Move",command = movefile).pack()
root.mainloop()