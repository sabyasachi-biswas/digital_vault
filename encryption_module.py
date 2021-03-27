import xor_module
import rsa_text
from tkinter import filedialog

def passcontrolencrypt(fileid,uid,algo,path):
    print(fileid,uid,algo,path)
    if algo == "XOR":
        xor_module.encrypt(path,int(uid)+int(fileid))
    if algo == "RSA":
        inputmsg=open(path,"r",encoding='utf-8')
        stringinput=inputmsg.read()
        cipher=rsa_text.encrypt(stringinput)
        filewrite=open(path,"w",encoding="utf-8")
        filewrite.write(cipher)
    
def passcontroldecrypt(fileid,uid,algo,path):
    print(fileid,uid,algo,path)
    if algo == "XOR":
        xor_module.decrypt(path,int(uid)+int(fileid))
    if algo == "RSA":
        inputmsg=open(path,"r",encoding='utf-8')
        stringinput=inputmsg.read()
        plaintext=rsa_text.decrypt(stringinput)
        filewrite=open(path,"w",encoding="utf-8")
        filewrite.write(plaintext)