#x = input("Enter URL/program: ")
#y = input("Enter Username: ")
#z = input ("Enter Password ")

#fileHandle = open("myFile.txt", "w")
#fileHandle.write(x + " " + y + " " + z + " ")

#fileHandle = open("myFile.txt", "r")
#data = fileHandle.read()
#data = data.split()

#print(f"{'first' : <30} ")

#i = 0
#while i < len(data):
    #print(f"{data[i+1] : ^100}")
    #i = i + 3

import os
if os.path.exists("myFile.txt"):
    print("file exists")
else:
    print("file does not exist")
    fileHandle = open("myFile.txt", "w")
    fileHandle.close()


