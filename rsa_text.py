import tkinter.filedialog as filedialog

file=filedialog.askopenfilename()
print(file)
inputmsg=open(file,"r",encoding='utf-8')
strinput=inputmsg.read()

m=strinput

n=65339
e=2575
d=11983

message_list = []
cypher_list = []

def encrypt(m):
    str1=''
    ASCII_values = []
    for character in m:
        ASCII_values.append(ord(character))
    for m in ASCII_values:
        c=(m**e)%n
        cypher_list.append(c)
    for i in cypher_list:
        str1=str1+chr(i)
    print(str1)
    return(str1)

def decrypt(m):
    str=''
    ASCII_values = []
    for character in m:
        ASCII_values.append(ord(character))
    for m in ASCII_values:
        message=(m**d)%n
        message_list.append(message)
    for i in message_list:
        str=str+chr(i)
    print(str)
    return(str)




filewrite=open(file,"w",encoding="utf-8")
filewrite.write(encrypt(m))