import csv ,os, validation as v, menus
import admin
import hashlib

def login(running = True):
    print("\n Q or q to quit")
    print("-------------- Login Page ----------------------")
    userdb_csv = r"LibraryManagement\LibM1\user_db.csv"
    file_exists = v.check_file_existance(userdb_csv)
    id_found = False
    fields = ["ID", "Role", "Username", "Password", "Status"]

    if not file_exists:
        #csv.DictReader(id_file, fieldnames=fieldnames ,delimiter=",")
        v.add_csv_header(userdb_csv, fields)

    if file_exists:
        while running:
            try:
                user_id = input("\nEnter Your ID: ").strip().upper()
                if not user_id:
                    raise ValueError("Please enter you user id!!!")
                running = v.breaking(user_id)
                user_id = v.int_check(user_id)
                if user_id:
                    with open(userdb_csv) as id_file:
                        user_data = csv.DictReader(id_file)

                        for row in (user_data): 
                            # the user_id must be in string format for checking
                            if row.get('U_ID')== user_id: 
                                id_found = True
                                for i in range (3,0,-1):
                                    try:
                                        #if id found ask pw
                                        pw = input("Enter your password: ")
                                        pw = hashlib.sha256(pw.encode()).hexdigest()
                                        #if row.get("Password")==pw
                                        if row['Password'] == pw:
                                            print("\nLogin\n")
                                            if row["Role"] =="Admin":
                                                menus.admin_dashboard()

                                            role = row["Role"]
                                            print("\n",role)
                                            
                                            exit()
                                            
                                        else:
                                            print("\nIncorrect Password!!!")
                                            print(f"You have {i-1} tries left")
                                            if i ==1:
                                                print(f"\nTry again later!!!")
                                                break
                                                
                                    except Exception as e:
                                        print(f"\nPassword error: {e}")     

                else: 
                    print("\nPlease enter ID in valid form")

                if not id_found:
                        print("\nID Not Found!!! \nPlease Enter Valid ID")

            except Exception as e:
                print(f"\nLogin Error: {e}")


login()