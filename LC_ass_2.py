def functionAdd():
    username = input('Username: ')
    password = input('Password: ')
    resource = input('URL/Resource: ')

functionAdd()
                                                #needs to write to txt file
import os                                       # this step is to check if txt file exists
if os.path.exists("myCredentials.txt"):         #problem with this 
    Credentials = open("myCredentials.txt", "a") 
    
else:
    Credentials = open("myCredentials.txt", "w")
    Credentials.close()

Credentials = open("myCredentials.txt", "r")    #read file
print(Credentials.read())                       #open file
Credentials = open("myCredentials.txt", "a")     #write/append file
Credentials.close()

def functionView():    
    credentials = open("myCredentials.txt", "r")   #open file
    data = Credentials.read()                      #read 

functionView()         #calling fnView

print(f"{'Username' : <20}{'Password' : ^30}{'URL/Resource' : >20}")       #display contents with 3 headings and spacings  

print(Credentials.read())
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
