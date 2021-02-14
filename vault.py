from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x250')
        self.title("DGITAL VAULT")
        Button(self,text="Print",command=lambda: print("Button is Clicked")).grid(row = 3, column =0,padx = 30,pady =10)




def start():
    root = GUI()
    root.mainloop()

