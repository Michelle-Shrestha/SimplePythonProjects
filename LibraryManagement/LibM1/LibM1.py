import csv ,os


def login():
    print("\nQ or q to quit")
    print("-------------- Login Page ----------------------")
    while True:
        try:
            
            user_id = input("\nPlease Enter Your ID: ").strip().upper()
            
            if user_id == "Q":
                print("Exiting the program")
                break

            elif user_id.isdigit():
                id_found = False
                userdb_csv = "LibraryManagement\LibM1\libM1_IDs.csv"

                if not os.path.isfile(userdb_csv):
                    print(f"Error: File {userdb_csv} not found")
                    continue

                with open(userdb_csv) as id_file:
                    #fieldnames = ["ID", "Role", "Username", "Password"]
                    user_data = csv.DictReader(id_file)
                    #csv.DictReader(id_file, fieldnames=fieldnames ,delimiter=",")

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


def admin_dashboard(): 
    print ("------ Admin Dashboard ------------")
    print("1. Books List")
    print("2. Edit book list")
    print("1. Add New Book")
    print("1. Add New Users")
    print("1. Edit Users List")


def user_db_headname():
    fields = ["ID", "Role", "Username", "Password"]
    filename = "LibraryManagement\LibM1\libM1_IDs.csv"
    file_exist = os.path.exists(filename)
    with open(filename, 'a') as userdb:
        write = csv.DictWriter(userdb, fieldnames= fields)
        if not file_exist:
            write.writeheader()
        #write.writerows

user_db_headname()

login()