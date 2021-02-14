from tkinter import *
# import vault


# def click():
#     print("clcik run")
#     root.destroy()
#     vault.start()
def rtclick(event):
    print("Right Clicked")  

root = Tk()

root.geometry('200x100')
button = Button(root, text = "Click")
button.bind("<Button-3>", rtclick)
button.pack()
label = Label(root, text = "Label", cursor="hand2",pady = 30)
label.bind("<Button-3>", rtclick)
label.pack()

root.mainloop()