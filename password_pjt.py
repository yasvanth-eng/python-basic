

passwords=[]

def add_password():
    website=(input("Enter the website :"))
    password=(input("Enter the password :"))
    
    
    password_dict={
         "website":website,
        "added password": password,
       
    }
    passwords.append(password_dict)    
    print("password added sucessfully")
    print("-"*85)

def view_added_password():
    if len(passwords) ==0:
        print("No passwords added yet")
        return
    for index, added_password in enumerate(passwords, 1):
        print("-" * 85)

        print("registered password:", added_password["password registered"])
        
        print("-" * 85)

while True:
    print("1. add password :")
    print("2. view password :")
    print("3. Exit")

    choice=(int(input("Enter the choice :")))

    if choice ==1:
         add_password()
    if choice ==2:
        view_added_password()
    if choice ==3:
        break
