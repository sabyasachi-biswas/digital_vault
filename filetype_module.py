import os.path
def checkfile(fileext):
    images=[".png",".jpg",".jpeg"]
    txt=[".txt"]
    if (fileext in images):
        print("Image")
    elif (fileext == ".txt"):
        print("Text")

def accept(filepath):
    fileext = os.path.splitext(filepath)
    checkfile(fileext[1])

# accept(input("Enter filepath"))