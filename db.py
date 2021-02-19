import sqlite3

conn = sqlite3.connect('user_data.db')
c = conn.cursor()
c.execute("""CREATE TABLE user  (
    uid integer NOT NULL PRIMARY KEY,
    name string,
    username string,
    pwd string
)""")
conn.commit()
conn.close()