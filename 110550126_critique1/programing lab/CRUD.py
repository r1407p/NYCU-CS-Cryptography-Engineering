import hasher
import elara
import maskpass
import string

def Authenticate(db):#verify whether is the owner of PM
    verify_master_password_unhashed =maskpass.askpass(prompt = "Enter master password for verification: ", mask = '*')
    verify_master_password = hasher.hash_master_password(verify_master_password_unhashed)
    return  verify_master_password == db.get("Masterpassword")
        
    
def new_password(db):
    website = input("Enter website for which password must be saved: ")
    password = maskpass.askpass(prompt = "Enter password to be saved: ")
    db.set(website, hasher.encode_password(password))
    print("Password added succesfully.")
    return db


def view_password(db):
    print("Websites for which passwords have been saved: ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j,end=". ")
        print(i)
        j+=1
    try:
        index = int(input("Enter website serial no. for which password is to be viewed: "))
    except:
        print("Please enter a number.")
        return
    if index<=0 or index>len(keys):
        print("Please enter a valid serial no.")
        return
    true_index = index-1 
    print("Password: "+hasher.decode_password(db.get(keys[true_index])))

    
def delete_password(db):
    print("Websites for which passwords have been saved: ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j,end=". ")
        print(i)
        j+=1
    try:
        index = int(input("Enter website serial no. for which password is to be deleted: "))
    except:
        print("Please enter a number.")
        return db
    if index<=0 or index>len(keys):
        print("Please enter a valid serial no.")
        return db
    
    if Authenticate(db):
        true_index = index-1 
        db.rem(keys[true_index])#delete website and password
        print("Password deletion succesful.")
    else:
        print("Authentication failed. Password not deleted.")
    return db

def update_password(db):
    print("Websites for which passwords have been saved: ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j,end=". ")
        print(i)
        j+=1
    try:
        index = int(input("Enter website serial no. for which password is to be updated: "))
    except:
        print("Please enter a number.")
        return db
    if index<=0 or index>len(keys):
        print("please enter a valid serial no.")
        return db
    if Authenticate(db):    
        newpass = maskpass.askpass(prompt = "Enter new password: ", mask = '*')
        true_index = index-1 
        db.set(keys[true_index], hasher.encode_password(newpass))
        print("Password updated succesful.")
    else:
        print("Authentication failed. Password not updated.")
        
    return db