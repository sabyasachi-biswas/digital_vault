import sqlite3

conn = sqlite3.connect('user_data.db')
c = conn.cursor()
# c.execute("""CREATE TABLE user  (
#     uid integer NOT NULL PRIMARY KEY,
#     name string,
#     username string,
#     pwd string
# )""")

# c.execute("""CREATE TABLE vault_config  (
#     uid integer NOT NULL PRIMARY KEY,
#     path string
# )""")

c.execute("""CREATE TABLE vault_data  (
    fileid integer NOT NULL PRIMARY KEY,
    uid integer NOT NULL,
    state string,
    filename string,
    path string,
    filetype string
)""")

conn.commit()
conn.close()