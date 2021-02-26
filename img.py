from PIL import Image,ImageTk
import tkinter.filedialog as filedialog
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    return(decrypted_message.decode())

def encrypt_message(encoded_message):
    """
    Encrypts a message
    """
    # generate_key()
    key = load_key()
    # encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    # print(encrypted_message)
    return(encrypted_message)

# if __name__ == "__main__":
#     encrypt_message("encrypt this message")

i=1
while i==1:
    ed=input("E/D")
    filename = filedialog.askopenfilename()
    if ed=="E":
        print(filename)
        file = open(filename,"rb")
        encrypted = encrypt_message(file.read())
        file = open(filename,"wb")
        file.write(encrypted)
    if ed =="D":
        file = open(filename,"rb")
        decrypted = decrypt_message(file.read())
        file = open(filename,"wb")
        file.write(decrypted)
    i=int(input("Exit with 0"))

# Img = Image.open(filename,'r')
# pix_val = list(Img.getdata())
# pix_val_flat = [x for sets in pix_val for x in sets]
# # for i in pix_val:
# #     for j in i:
# #         print(pix_val[j])
# print(pix_val_flat)