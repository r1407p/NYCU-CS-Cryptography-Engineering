import json
import elara
import hashlib
import maskpass
import hasher
import CRUD
from hasher import decode_password, encode_password, hash_master_password


def set_master_password():
    master_password = maskpass.askpass(prompt = "Set Master Password: ", mask = '*')
    return hash_master_password(master_password)



def intialise_db():
    db = elara.exe_secure("data.db", True)
    #db.rem("Masterpassword")
    if not db.exists("Masterpassword"):
        db.set("Masterpassword", set_master_password())
    return db



if __name__ =="__main__":
    db = intialise_db()
    if CRUD.Authenticate(db):
        print("Hi! Please select an option you want to continue with: ")
        while(1):
            print(" ")
            print("1. Add a new password")
            print("2. View a password")
            print("3. Update a password") 
            print("4. Delete a password") 
            print("5. Exit ")
            print(" ")

            choice = int(input("Enter option number: "))
            if choice == 1:
                db = CRUD.new_password(db)
            elif choice == 2:
                CRUD.view_password(db)
            elif choice == 3:
                db = CRUD.update_password(db)
            elif choice == 4:
                db = CRUD.delete_password(db)
            elif choice == 5:
                print(" ")
                print("Thanks for your using.")
                break
            else:
                print("Invalid choice. Please select a valid choice")
    else:
        print("Authentication failed.")
