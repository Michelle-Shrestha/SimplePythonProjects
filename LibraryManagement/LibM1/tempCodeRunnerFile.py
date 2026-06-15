import csv ,os, validation as v



def login():
    print("\nQ or q to quit")
    print("-------------- Login Page ----------------------")
    userdb_csv = r"LibraryManagement\LibM1\user_db222222222.csv"
    file_exists = v.check_file_existance(userdb_csv)
    id_found = False
    fields = ["ID", "Role", "Username", "Password", "Status"]

    if not file_exists:
        #csv.DictReader(id_file, fieldnames=fieldnames ,delimiter=",")
        v.add_csv_header(userdb_csv, fields)

    while file_exists:
        try:
            user_id = input("\nPlease Enter Your ID: ").strip().upper()
                
            if user_id == "Q":
                print("Exiting the program")
                break

            elif user_id.isdigit():
                with open(userdb_csv) as id_file:
                    user_data = csv.DictReader(id_file)

                    for row in (user_data): 
                        # the user_id must be in string format for checking
                        if row.get('ID')== user_id: 
                            id_found = True
                            for i in range (3,0,-1):
                                try:
                                    #if id found ask pw
                                    pw = input("Enter your password: ")
                                    #if row.get("Password")==pw
                                    if row['Password'] == pw:
                                        print("\nLogin\n")
                                        exit()
                                            
                                    else:
                                        print("\nIncorrect Password!!!")
                                        print(f"You have {i-1} left")
                                        if i ==1:
                                            print(f"\nTry again later!!!")
                                            break
                                            
                                except Exception as e:
                                    print(f"\nPassword error: {e}")
                                
                            
                if not id_found:
                    print("\nID Not Found!!! \nPlease Enter Valid ID")

            else: 
                print("\nPlease enter ID in valid form")

        except Exception as e:
            print(f"\nLogin Error: {e}")


login()