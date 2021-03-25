import tkinter.filedialog as filedialog
import PIL.Image


filepath = filedialog.askopenfilename()
print(filepath)


file = open(filepath,"rb")
print(file)
img = PIL.Image.open(file)
img.show()
