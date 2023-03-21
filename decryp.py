import os
from cryptography.fernet import Fernet
import tkinter
from tkinter import filedialog as fd

fileLists = []
if os.path.exists('key.key'):
    key = open("key.key", "rb").read()

dirtodecrypt= 'testfolder'

def choseFile():
    global key
    fileread=fd.askopenfilename(filetypes =[('Key Files', '*.key')])
    tf = open(fileread, 'rb')
    key = tf.read()

def choseDir():
    global dirtodecrypt
    dirtodecrypt=fd.askdirectory(parent=root,initialdir="/",title='Pick a directory')

def decrypterFindFile():
    for (root,dirs,file) in os.walk(dirtodecrypt, topdown=True):
        for files in file:
            if files.endswith(EXT):
                files = os.path.join(root, files)
                fileLists.append(files)

def decryptme():
    global EXT
    EXT = EXT_entry.get()
    if not EXT:
        EXT = ".sasa"
    decrypterFindFile()
    for files in fileLists:
        with open(str(files), "rb") as f:
            data = f.read()
        with open(str(files), "wb") as f:
            decryptedData = Fernet(key).decrypt(data)
            f.write(decryptedData)
        os.rename(str(files), files.split(EXT)[0])
    root.quit()

if 1:
    root=tkinter.Tk()
    root.title('Fernet decrypter')
    root.geometry('350x250')
    root.resizable(0,0)
    tkinter.Label(root,text=f' Made by Sabbir Ahmed\ngithub.com/sabbir-21\n\nHelp: Default is key.key in current dir\nDefault directory "testfolder"',font= ("Times New Roman", 10)).pack()
    tkinter.Label(root, text='Enter Crypter extention:',fg='green').pack()
    EXT_entry = tkinter.Entry(root, width=15)
    EXT_entry.insert(0, '.sasa')
    EXT_entry.pack(pady=5)
    tkinter.Button(root,text='Select  the  key ',command=choseFile).pack(pady=1)
    tkinter.Button(root,text='Select Directory',command=choseDir).pack(pady=1)
    tkinter.Button(root,text='Decrypt my files',command=decryptme, fg='white', bg='green').pack(pady=15)
    root.mainloop()
