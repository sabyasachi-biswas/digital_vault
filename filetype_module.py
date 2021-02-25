import os.path
import ntpath
def checkfile(fileext):
    images=[".png",".jpg",".jpeg"]
    txt=[".txt"]
    if (fileext in images):
        print("Image")
    elif (fileext == ".txt"):
        print("Text")

def filename(fileext):
    return(ntpath.basename(fileext))

def accept(filepath):
    fileext = os.path.splitext(filepath)
    checkfile(fileext[1])

# accept(input("Enter filepath"))