import xor_module

def passcontrolencrypt(fileid,uid,algo,path):
    print(fileid,uid,algo,path)
    if algo == "XOR":
        xor_module.encrypt(path,int(uid)+int(fileid))

def passcontroldecrypt(fileid,uid,algo,path):
    print(fileid,uid,algo,path)
    if algo == "XOR":
        xor_module.decrypt(path,int(uid)+int(fileid))