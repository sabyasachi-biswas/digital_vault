import tkinter.filedialog as filedialog

file=filedialog.askopenfilename()
inputmsg=open(file,"rb")
strinput=inputmsg.read()
print(strinput)
strinput=bytearray(strinput)
writestr=''
empty=[]
for i,value in enumerate(strinput):
    empty.append(strinput[i])

# print(empty)
for i,value in enumerate(empty):
    empty[i]+=1
# print(empty)
for i,value in enumerate(empty):
    empty[i]-=1

for i,value in enumerate(empty):
    writestr+=str(empty[i])
# print(writestr)

# file=filedialog.askopenfilename()
# inputmsg=open(file,"wb")
# inputmsg.write(strinput)
new_array = bytearray()
# for i,value in enumerate(empty):
    # new_array.append(str(empty[i]))
    # new_array.append(bytes(empty[i]))
new_array.append()
# new_array = bytearray(empty.encode())
print(new_array)