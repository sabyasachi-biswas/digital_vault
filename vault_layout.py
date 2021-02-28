from tkinter import Tk, Text, BOTH, W, N, E, S, ttk
from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
import tkinter.filedialog as filedialog
import filetype_module
import sqlite3
import shutil
import os


class Example(Frame):

    def __init__(self,uid):
        super().__init__()
        self.uid=uid
        self.initUI()


    def initUI(self):
        self.master.geometry("700x900")
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

        


        self.treev_encrypt = ttk.Treeview(self,height = 15, selectmode = "browse")
        self.treev_encrypt.grid(row = 1, column = 0,columnspan=2, rowspan=4,padx=5,pady=5,sticky=E+W+S+N)

        lbl = Label(self, text="Decrypted")
        lbl.grid(row = 5,column = 0,sticky=W, pady=4, padx=5)

        self.treev_decrypt = ttk.Treeview(self,height = 17, selectmode = "browse")
        self.treev_decrypt.grid(row = 6, column = 0,columnspan=2, rowspan=4,padx=5,pady=5,sticky=E+W+S+N)

        btn_addfile = Button(self, text="Add File",command = self.addfile)
        btn_addfile.grid(row=1, column=5, pady=5,padx = 10)

        abtn = Button(self, text="Encrypt",command = self.encrypt)
        abtn.grid(row=2, column=5, pady=5,padx = 10)

        btn_decrypt = Button(self, text="Decrypt",command = self.decrypt)
        btn_decrypt.grid(row=3, column=5, pady=10,padx = 10)

        
            
        hbtn = Button(self, text="Refresh",command = self.refresh_decrypt)
        hbtn.grid(row=10, column=0, pady=10,padx = 2)

        obtn = Button(self, text="View")
        obtn.grid(row=10, column=5, pady=10,padx = 10)

        lbl = Label(self, text="USERNAME")
        lbl.grid(sticky=W)
        lbl = Label(self, text="label")
        lbl.grid(sticky=W)
        lbl = Label(self, text="label2")
        lbl.grid(sticky=W)

        self.refresh_decrypt()

    def decrypt(self):
        self.refresh_decrypt()

    def refresh_decrypt(self):
        conn=sqlite3.connect('user_data.db')
        c = conn.cursor()

        # To avoid duplicate values in treeview
        for record in self.treev_decrypt.get_children():
            self.treev_decrypt.delete(record)

        self.treev_decrypt["columns"] = ("1", "2", "3","4")
        self.treev_decrypt['show'] = 'headings'

        self.treev_decrypt.column("1", width = 70)

        self.treev_decrypt.heading("1", text ="File ID") 
        self.treev_decrypt.heading("2", text ="File") 
        self.treev_decrypt.heading("3", text ="Size (KB)")
        self.treev_decrypt.heading("4", text ="Type")

        state="Decrypted"

        c.execute("SELECT fileid FROM vault_data where uid=(:uid)  AND state=(:state)",{
            'uid' : self.uid,
            'state' : state
        })
        fileid=c.fetchall()
        c.execute("SELECT filename FROM vault_data where uid=(:uid) AND state=(:state)",{
            'uid' : self.uid,
            'state' : state
        })
        filename=c.fetchall()
        c.execute("SELECT filesize FROM vault_data where uid=(:uid) AND state=(:state)",{
            'uid' : self.uid,
            'state' : state
        })
        filesize=c.fetchall()
        c.execute("SELECT filetype FROM vault_data where uid=(:uid) AND state=(:state)",{
            'uid' : self.uid,
            'state' : state
        })
        filetype=c.fetchall()
        c.execute("SELECT COUNT(*) FROM vault_data where state=(:state)",{
            'state' : state
        })
        count=c.fetchone()

        for i in range(0,count[0]):
            local_filename = filename[i]
            dummy_filesize = filesize[i]
            local_filesize = dummy_filesize[0]/1024
            self.treev_decrypt.insert("", 'end', text ="L1",  
                    values =(fileid[i], local_filename[0],  round(local_filesize,2), filetype[i]))

        conn.commit()
        conn.close()

    def addfile(self):
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        #-----Moving File-----------
        c.execute("SELECT path FROM vault_config WHERE uid=(:uid)",{
            'uid' : self.uid
        })
        dest_path = c.fetchone()
        print(dest_path[0])

        #---------------------------
        self.addfilename = filedialog.askopenfilename()

        filetype=filetype_module.checkfile(self.addfilename)
        print(filetype)
        filename=filetype_module.filename(self.addfilename)
        filesize=filetype_module.filesize(self.addfilename)
        # print(filesize)

        shutil.move(self.addfilename,dest_path[0])
        filepath = os.path.join(dest_path[0],filename)

        state="Decrypted"
        algo="none"
        c.execute("INSERT INTO vault_data (uid, state, algo, filename, filesize, path, filetype) VALUES (:uid,:state,:algo,:filename,:filesize,:path,:filetype)",{
            'uid' : self.uid,
            'state' : state,
            'algo' : algo,
            'filename' : filename,
            'filesize' : filesize,
            'path' : filepath,
            'filetype' : filetype
        })

        conn.commit()
        conn.close()

        self.refresh_decrypt()

    def encrypt(self):
        def ok():
            print(value.get())
        encrypt_window = Toplevel(self)
        encrypt_window.geometry("200x200")
        # list = ["AES-128","AES-192","AES-256","RSA"]
        self.value=StringVar()
        combobox = ttk.Combobox(encrypt_window,textvariable=self.value,state='readonly')
        combobox['values'] = ('AES-128','AES-192','AES-256','RSA')
        combobox.current(0)
        combobox.grid(pady = 10,padx = 10)
        button=Button(encrypt_window,text="OK",command=self.refresh_encrypt).grid()
        
    def refresh_encrypt(self):
        print(self.value.get())
        try:
            Item = self.treev_decrypt.focus()
            localval = self.treev_decrypt.item(Item, 'values')
            print (localval[0])
        except IndexError:
            print("Please select something")
        

def start(uid):

    root = Tk()
    app = Example(uid)
    root.mainloop()

start(1)