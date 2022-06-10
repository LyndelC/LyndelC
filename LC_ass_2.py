def functionAdd():
    username = input('Username: ')
    password = input('Password: ')
    resource = input('URL/Resource: ')

functionAdd()

import os                                       # to check if txt file exists
if os.path.exists("myCredentials.txt"):
    fileHandle = open("myCredentials.txt, "a") #fileHandle not recognised, need file name and file
else:
    fileHandle = open("myCredentials.txt", "w")
    fileHandle.close()
    ")

#myCredentials = open("myCredentials.txt", "r") #must change fileHandle name
#print(myCredentials.read())open file
#fileHandle = open("myCredentials.txt, "a")     #write file, change file and functioin
#myCredentials.close()

#def functionView():    
    #credentialFile = open("myCredentials.txt", "r")  #open file
    #data = myCredentials.read()#read 

#functionView()         #calling fnView
#print(f"{'Username : <20} {'Password' : ^30} {'URL/Resource' : >20}")            #display contents with 3 headings and spacings  

    #myCredentials = ["Add", "View", "Edit"]  #while loop needs refined for menu options
    #i = 0
    #while i < len(myCredentials):
        #print(myCredentials[i])
        #i = i + 1


    #while/for ?what is the T/F here?
        #print("\n Press 1 to add credentials \n" + "\n Press 2 to view credentials \n” + "\n Press 3 to exit \n”) 
        #if 1: 
            #functionAdd()
        #if 2: 
            #functionView()
        #if 3: 
            #exit()
        #else:
            #print(“Invalid entry")
