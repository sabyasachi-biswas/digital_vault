import tkinter.filedialog as filedialog

# file=filedialog.askopenfilename()
# print(file)
# inputmsg=open(file,"r",encoding='utf-8')
# strinput=inputmsg.read()
n=65339
e=2575
d=11983




def encrypt(input_string):
    str1=''
    ASCII_values = []
    cypher_list = []
    ASCII_values.clear()
    cypher_list.clear()
    
    for character in input_string:
        ASCII_values.append(ord(character))
    for m in ASCII_values:
        c=(m**e)%n
        cypher_list.append(c)
    for i in cypher_list:
        str1=str1+chr(i)
    # print(str1)
    return(str1)

def decrypt(input_string):
    str=''
    ASCII_values = []
    message_list = []
    ASCII_values.clear()
    message_list.clear()
    for character in input_string:
        ASCII_values.append(ord(character))
    for m in ASCII_values:
        message=(m**d)%n
        message_list.append(message)
    for i in message_list:
        str=str+chr(i)
    # print(str)
    return(str)




