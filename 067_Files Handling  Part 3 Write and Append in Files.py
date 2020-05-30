# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myFile = open("mido.txt", "w")
myFile.write("=" * 50)
myFile.write("\nHello\n")
myFile.write("Third Line\n")
myFile.write("=" * 50)

myFile = open(r"fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("mido.txt", "w")
myFile.writelines(myList)

myFile = open("mido.txt", "a")
myFile.write("Elzero")
