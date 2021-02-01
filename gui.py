from tkinter import *
from tkinter.font import Font

# ------------------Geometry------------------------------------------
login_page = Tk()
login_page.geometry('500x250')
login_page.minsize(400,170)

# ------------------Header--------------------------------------------
font_head = Font(family = "", weight = "bold", size = 20)

#-------------------Buttons,Labels,etc..------------------------------
label_text = Label(login_page, text = "Login Page", anchor = CENTER, font = font_head)
label_text.pack()
#username_frame
frame_username = Frame(login_page)
frame_username.pack()

label_login = Label(frame_username, text = "Username")
label_login.pack(side = LEFT)
entry_username = Entry(frame_username)
entry_username.pack()
#password_frame
frame_password = Frame(login_page)
frame_password.pack()

label_password = Label(frame_password, text = "Password")
label_password.pack(side = LEFT)
entry_password = Entry(frame_password, show = "*")
entry_password.pack()
#button_frame
frame_button = Frame(login_page)
frame_button.pack()

btn_login = Button(frame_button, text = "LOGIN")
btn_login.pack(side = LEFT)
btn_register = Button(frame_button, text = "REGISTER")
btn_register.pack(side = BOTTOM)


login_page.mainloop()