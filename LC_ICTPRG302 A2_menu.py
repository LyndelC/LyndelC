print("\nThis program is intended to securely store the usernames and passwords for your URLs/resources.\n")

def Add():
    print("\nEnter username, password and URL/resource\n")
    user = input('Username:  ')
    pw = input('Password:  ')
    res = input('URL/Resource:  ')
    Credentials = open("myCredentials.txt", "a")        #if the txt file doesn't exist, open function will create a new one
    
    Credentials.write("Username: ")
    Credentials.write(user) 
    Credentials.write("\n") 

    Credentials.write("Password: ")                              
    Credentials.write(pw)
    Credentials.write("\n") 

    Credentials.write("Resource: ")
    Credentials.write(res) 
    Credentials.write("\n\n")                           
    Credentials.close()  
    
def View():     
    Credentials = open("myCredentials.txt", "a")            #open txt file if one doesn't already exist
    Credentials.close()    

    Credentials = open("myCredentials.txt", "r")                         
    print(Credentials.read())
    Credentials.close()   

choice = ''  

# Set an initial value for choice other than the value for 'quit'.
while choice != 'q':
    print("\nOptions: ")                           
    print("[1] Enter 1 to add your credentials ")
    print("[2] Enter 2 to view your credentials ")
    print("[q] Enter q to quit")

    choice = input("\nChoose 1, 2 or q: ")                                  # Ask for the user's choice.

    if choice == '1':                                                       #  Respond to the user's choice. 
        Add()                
    elif choice == '2':
        View()                           
    elif choice == 'q':
        print("\nExit\n")  
    else:
        print("\nInvalid entry, please try again.\n")          
         
print("Document is now closed")

