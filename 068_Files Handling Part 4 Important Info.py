# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open("mido.txt", "a")
myFile.truncate(5)

myFile = open("mido.txt", "a")
print(myFile.tell())

myFile = open("mido.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove("mido.txt")
