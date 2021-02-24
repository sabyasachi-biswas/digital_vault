from tkinter import Tk, Text, BOTH, W, N, E, S, ttk
from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.master.geometry("700x820")
        self.master.title("Windows")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        # 
        # self.rowconfigure(3, weight=1)
        # self.rowconfigure(5, pad=7)

        

        # area = Text(self)
        # area.grid(row=1, column=0, columnspan=2, rowspan=4,
        #     padx=5, sticky=E+W+S+N)

        lbl = Label(self, text="Encrypted")
        lbl.grid(row = 0,column = 0,sticky=W, pady=10, padx=5)

        


        treev = ttk.Treeview(self,height = 15, selectmode = "browse")
        treev.grid(row = 1, column = 0,columnspan=2, rowspan=4,padx=5,pady=5,sticky=E+W+S+N)

        lbl = Label(self, text="Decrypted")
        lbl.grid(row = 5,column = 0,sticky=W, pady=4, padx=5)

        treev2 = ttk.Treeview(self,height = 17, selectmode = "browse")
        treev2.grid(row = 6, column = 0,columnspan=2, rowspan=4,padx=5,pady=5,sticky=E+W+S+N)

        abtn3 = Button(self, text="Add File")
        abtn3.grid(row=1, column=5, pady=10,padx = 10)

        abtn = Button(self, text="Encrypt",command = self.encrypt)
        abtn.grid(row=2, column=5, pady=10,padx = 10)

        cbtn = Button(self, text="Decrypt")
        cbtn.grid(row=3, column=5, pady=10,padx = 10)

        
            
        hbtn = Button(self, text="Help")
        hbtn.grid(row=10, column=0, pady=10,padx = 2)

        obtn = Button(self, text="View")
        obtn.grid(row=10, column=5, pady=10,padx = 10)

        lbl = Label(self, text="USERNAME")
        lbl.grid(sticky=W)
        lbl = Label(self, text="label")
        lbl.grid(sticky=W)
        lbl = Label(self, text="label2")
        lbl.grid(sticky=W)
    
    def encrypt(self):
        def ok():
            print(value.get())
        encrypt_window = Toplevel(self)
        encrypt_window.geometry("200x200")
        list = ["AES-128","AES-192","AES-256","RSA"]
        value=StringVar()
        combobox = ttk.Combobox(encrypt_window,textvariable=value,state='readonly')
        combobox['values'] = ('AES-128','AES-192','AES-256','RSA')
        combobox.current(0)
        combobox.grid(pady = 10,padx = 10)
        button=Button(encrypt_window,text="OK",command=ok).grid()
        

def main():

    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()