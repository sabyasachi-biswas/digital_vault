from PIL import Image
from numpy import asarray
import tkinter.filedialog as filedialog

file=filedialog.askopenfilename()
img = Image.open(file)
  
numpydata = asarray(img)
  
# data

# print(numpydata)
# print(len(numpydata.shape))
for i,val in enumerate(numpydata):
    for j,val2 in enumerate(val):
        numpydata[i][j]=numpydata[i][j]+102

print(numpydata)
# img.show()