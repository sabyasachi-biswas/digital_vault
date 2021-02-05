import bcrypt

def hashpwd(password):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def checkpwd(entered_pwd,password):
    if bcrypt.checkpw(entered_pwd,password):
        return True
    else:
        return False