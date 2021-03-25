import tkinter.filedialog as filedialog

def encrypt(file,key):
    try:

        path = file
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)
    
        for index, values in enumerate(image):
            image[index] = values ^ key
    
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()

        print("Encryption Done")
        
    except Exception:
        print('Error caught : ', Exception.__name__)

def decrypt(file,key):
    try:
        path = file        
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)

        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')
        fin.write(image)
        fin.close()   
        print("Decryption done")
        
    except Exception:
        print('Error caught : ', Exception.__name__)

