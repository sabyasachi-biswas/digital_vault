from tkinter import *
from PIL import Image,ImageTk
import tkinter.filedialog as filedialog
from tkinter.font import Font
from tkinter import ttk
import sqlite3
import filetype_module

class GUI(Tk):
    def __init__(self,uid):
        self.uid = uid
        super().__init__()
        conn = sqlite3.connect("user_data.db")
        c = conn.cursor()
        self.filename = "seal.jpg"
        myfont=Font(underline=1)
        print(self.uid)
        def openimg():
            self.label = Label(self, text = "")
            self.filename = filedialog.askopenfilename()
            print(self.filename)
            filetype_module.accept(self.filename)
            self.file = open(self.filename,"rb")
            self.Img = ImageTk.PhotoImage(Image.open(self.file))
            self.label = Label(self, image = self.Img)
            self.label.grid(row = 1,column = 1)
        def prep(event):
            print("Label clicked")
        def change_path():
            connection = sqlite3.connect("user_data.db")
            c = connection.cursor()
            filepath = filedialog.askdirectory()
            print(filepath)
            c.execute("SELECT EXISTS(SELECT 1 FROM vault_config WHERE uid=(:uid))",{
            'uid' : self.uid
            })
            bool = c.fetchone()
            if (bool[0] == 1):
                print(self.uid)
                c.execute("UPDATE vault_config SET path=(:filepath) WHERE uid=(:uid)",{
                'filepath' : filepath,
                'uid' : self.uid
                })
                print("If block")
            else:
                c.execute("INSERT INTO vault_config (uid, path) VALUES (:uid, :filepath)",{
                    'uid' : self.uid,
                    'filepath' : str(filepath)
                })
                print("Else block")

            connection.commit()   
            connection.close()


        self.geometry('800x550')
        self.title("DGITAL VAULT")

        self.btn = Button(self,text = "Open",command = openimg).grid(row = 0, column = 1,pady =10,padx =10)
        self.button_change_path = Button(self,text = "Change Path",command = change_path).grid(row = 1, column = 1,pady =10,padx =10)
        self.label = Label(self,text = "Click",font=myfont,cursor="hand2",fg="green")
        self.label.bind("<Button-3>", prep)
        self.label.grid(row = 2, column = 1,pady =30,padx =30)
        self.treev = ttk.Treeview(self, selectmode="browse")
        self.treev.grid(row = 0, column = 3,columnspan = 3,pady =30,padx =30)
        self.treev["columns"] = ("1", "2", "3")
        self.treev['show'] = 'headings'

        # Assigning the width and anchor to  the 
        # respective columns 
        self.treev.column("1", width = 50, anchor ='c') 
        self.treev.column("2", width = 90, anchor ='se') 
        self.treev.column("3", width = 150, anchor ='se') 
        
        # Assigning the heading names to the  
        # respective columns 
        self.treev.heading("1", text ="uid") 
        self.treev.heading("2", text ="username") 
        self.treev.heading("3", text ="pwd") 
        
        # Inserting the items and their features to the  
        # columns built 
        c.execute("SELECT username FROM user where uid=(:uid)",{
            'uid' : self.uid
        })
        user = c.fetchall()
        c.execute("SELECT uid FROM user where uid=(:uid)",{
            'uid' : self.uid
        })
        usid = c.fetchall()
        c.execute("SELECT pwd FROM user where uid=(:uid)",{
            'uid' : self.uid
        })
        upwd = c.fetchall()
        c.execute("SELECT COUNT(*) FROM user")
        count = c.fetchone()

        # for record in user:
        for i in range(0,count[0]):
            self.treev.insert("", 'end', text ="L1",  
                    values =(usid[0], user[0],  upwd[0])) 

        conn.commit()
        conn.close()
        
        
        
    
def start(uid):
    root = GUI(uid)
    root.mainloop()
 
start(2)
