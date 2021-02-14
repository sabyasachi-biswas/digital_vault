from tkinter import *
import vault

def click():
    print("clcik run")
    root.destroy()
    vault.start()
    

root = Tk()

root.geometry('200x100')

button = Button(root, text = "Click", command =click)
button.pack()

root.mainloop()