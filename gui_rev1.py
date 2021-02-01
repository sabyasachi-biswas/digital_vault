from tkinter import *
from tkinter.font import Font

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x250+500+300')
        self.resizable(False,False)
        self.title("Login")
        # ------------------Header--------------------------------------------
        font_head = Font(family = "", weight = "bold", size = 20)
        #-------------------Buttons,Labels,etc..------------------------------
        label_text = Label(self, text = "Digital Vault", anchor = CENTER, font = font_head)
        label_text.pack(pady = 10)
        #username_frame
        frame_username = Frame(self)
        frame_username.pack()

        label_login = Label(frame_username, text = "Username")
        label_login.pack(side = LEFT)
        entry_username = Entry(frame_username)
        entry_username.pack()
        #password_frame
        frame_password = Frame(self)
        frame_password.pack(pady = 5)

        label_password = Label(frame_password, text = "Password")
        label_password.pack(side = LEFT)
        entry_password = Entry(frame_password, show = "*")
        entry_password.pack()
        #button_frame
        frame_button = Frame(self)
        frame_button.pack(pady = 5)

        btn_login = Button(frame_button, text = "LOGIN", command = self.validation_check)
        btn_login.pack(pady = 5,padx = 10)

        btn_register = Button(frame_button, text = "REGISTER", command = self.user_register)
        btn_register.pack(pady = 5,padx = 10)
    def validation_check(self):
            error_window = Toplevel(self)
            error_window.geometry('250x50')
            error_window.title("Error")
            error_window.resizable(False,False)
            error_label = Label(error_window, text = "Incorrect Username or Password", foreground = "red")
            error_label.pack()

    def user_register(self):
        print("Register butoon clicked")
        register_window = Toplevel(self)
        register_window.title("Register")
        register_window.geometry('300x250')
        #regname_frame
        frame_regname = Frame(register_window)
        frame_regname.pack()

        label_regname = Label(frame_regname, text = "Username")
        label_regname.pack(side = LEFT)
        self.entry_regname = Entry(frame_regname)
        self.entry_regname.pack()
        #regpassword_frame
        frame_regpassword = Frame(register_window)
        frame_regpassword.pack()

        label_regpassword = Label(frame_regpassword, text = "Password")
        label_regpassword.pack(side = LEFT)
        self.entry_regpassword = Entry(frame_regpassword, show = "*")
        self.entry_regpassword.pack()
        #confirmpassword_frame
        frame_confirmpassword = Frame(register_window)
        frame_confirmpassword.pack()

        label_confirmpassword = Label(frame_confirmpassword, text = "Confirm Password")
        label_confirmpassword.pack(side = LEFT)
        self.entry_confirmpassword = Entry(frame_confirmpassword, show = "*")
        self.entry_confirmpassword.pack()
        #get_values
        self.regpassword = (self.entry_regpassword.get())
        self.confirmpassword = (self.entry_confirmpassword.get())
        
        #button_frame
        frame_regbutton = Frame(register_window)
        frame_regbutton.pack()
        btn_reglogin = Button(frame_regbutton, text = "REGISTER",command = self.register)
        btn_reglogin.pack(side = LEFT)

    def register(self):
        password = self.entry_regpassword.get()
        confirm_password = self.entry_confirmpassword.get()
        if password == confirm_password:
            print("True")
        else:
            error_window = Toplevel(self)
            error_window.title("Error")
            error_window.geometry('250x50')
            error_window.resizable(False,False)
            error_label = Label(error_window, text = "Password doesn't match", foreground = "red")
            error_label.pack()
                

root = GUI()

root.mainloop()