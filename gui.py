from tkinter import *
from tkinter.font import Font

# ------------------Header------------------------------------------
font_head = Font(family = "", weight = "bold", size = 20)

# ------------------Geometry------------------------------------------
root = Tk()
root.geometry('700x500')

label_text = Label(root, text = "Login Page", anchor = CENTER, font = font_head)
label_text.pack()


root.mainloop()