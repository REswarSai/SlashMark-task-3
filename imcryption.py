from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("200x160")

def encrypt_image():
    file1=filedialog.askopenfile(mode='r',filetype=[('png file','*.png'),('jpg file','*.jpg'),('jpeg file','*.jpeg')])
    if file1 is not None:
        #print(file1)
        file_name=file1.name
        #print(file_name)
        key=input1.get(1.0,END)
        print(file_name,key)
        f=open(file_name,'rb')
        image=f.read()
        f.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)  #As we are using XOR operations here, for the first time it will be encrypting with the given key and then for second time it will be decrypting with the same key used for encrypting.
        f1=open(file_name,'wb')
        f1.write(image)
        f1.close()

b1=Button(root,text="encrypt",command=encrypt_image)
b1.place(x=75,y=20)

input1=Text(root,height=1,width=10)
input1.place(x=60,y=60)

root.mainloop()