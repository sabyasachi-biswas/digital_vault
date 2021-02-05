from tkinter import *
import sqlite3
import hashing


root = Tk()
root.title("Database App")
root.geometry('400x150+700+300')



def submit():
    conn = sqlite3.connect('hash_table.db')
    string1 = str.encode(f_name.get())
    value = hashing.hashpwd(string1)
    c = conn.cursor()
    c.execute("INSERT INTO hash_val VALUES(:f_name)",{
        'f_name' : value
    })

    conn.commit()
    conn.close()
    f_name.delete(0, END)
    # l_name.delete(0, END)
    # pin.delete(0, END)

def printout():
    conn = sqlite3.connect('hash_table.db')

    new_hash = str.encode(l_name.get())
    c = conn.cursor()
    c.execute("SELECT value FROM hash_val")
    data = c.fetchall()
    for record in data:
        # print(str(record[0]))
        # if new_hash == record[0]:
        #     print(True)
        hashing.checkpwd(new_hash,record[0])
    conn.commit()
    conn.close()

    


conn = sqlite3.connect('hash_table.db')

c = conn.cursor()
# c.execute("""CREATE TABLE hash_val  (
#     value string
# )""")
conn.commit()
conn.close()
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 0, pady = 20, padx = 5)
l_name = Entry(root, width = 30)
l_name.grid(row = 0, column = 1, pady = 20, padx = 5)
# pin = Entry(root, width = 30)
# pin.grid(row = 0, column = 2, padx = 5)

f_name_label = Label(root, text = "String")
f_name_label.grid(row = 1, column = 0)
l_name_label = Label(root, text = "check")
l_name_label.grid(row = 1, column = 1)
# pin_label = Label(root, text = "Pincode")
# pin_label.grid(row = 1, column = 2)

btn = Button(root, text = "Add Record", command = submit)
btn.grid(row = 2, column = 1)

btn_print = Button(root, text = "Check", command = printout)
btn_print.grid(row = 3, column = 1)


root.mainloop()