import os, csv, pandas as pd 
import validation as v, menus as m #importing local py files


def user_details():
    path = r"LibraryManagement\LibM1\user_db.csv"
    c = 10
    print("\n1. To View first All User")
    print(f"2. To View first {c} users")
    print(f"3. To View Last {c} user")
    
    try:
        user_input = int(input("\nEnter your choice: "))
        v.breaking(user_input)
        print("\n Users: ")
        print()
        
        df = pd.read_csv(path)
        if user_input ==1:
            print(pd.DataFrame(df))
        elif user_input ==2:
            print(df.head(c))
        elif user_input ==3:
            print(df.tail(c))
        else:
            print("Select from the given options!!!")
    except pd.errors.EmptyDataError:
        print(f"\n {path} file is empty")

    except Exception as e:
        print(f"\n Undexpected error: {e}")


def add_user():
    user_path = r"LibraryManagement\LibM1\user_db.csv"
    file_exists = v.check_file_existance(user_path)
    fields = ["U_ID", "Username","Role", "Password", "Status", "Created Date"]
    if not file_exists:
        v.add_csv_header(user_path, fields)

    if file_exists:
        with open(user_path, mode= "a+", newline="") as user_file:
            db_write = csv.DictWriter(user_file, fieldnames=fields)
            c_date = v.curr_date_time()
            u_id = v.valid_id(user_path, "U_ID")
            u_name = v.validate_username()
            role = v.valid_role()
            pw = v.validate_password()
            status = v.valid_status()

            try:
                new_user ={
                    "U_ID" : u_id +1,
                    "Username": u_name,
                    "Role": role,
                    "Password": pw,
                    "Status": status,
                    "Created Date": c_date
                    }

                db_write.writerow(new_user)
                print(f"\n{role} Added Successfully")
            except Exception as e:
                print(f"Adding user error: {e}")
         
def delete_users():
    user_path = r"LibraryManagement\LibM1\user_db.csv"
    file_exists = v.check_file_existance(user_path)

    if  file_exists:
            try:
                del_id= input("\nUser ID to delete: ").upper()
                v.breaking(del_id)
                df = pd.read_csv(user_path)
                if del_id.isdigit():
                    try:
                        del_id = int(del_id)
                        if del_id not in df["U_ID"].values:
                            print(f"\nID {del_id} does not exists")
                        else:
                            df =df[df["U_ID"]!=del_id]
                            df.to_csv(user_path, index=False)
                            print(f"\nID {del_id} Deleted Successfully")

                    except ValueError as ve:
                        print(f"\n Deleter User Data Type Error: {ve}")
            except Exception as e:
                print(f"\n Delete User Error: {e}")

#def edit_users():

# ------------------------------------------------------------------ Book ------------------------------------------------------------------------------------

def book_details(role):
    path = r"LibraryManagement\LibM1\books.csv"
    try: 
        columns = ['B_ID', 'Title', 'ISBN', 'Author', 'Published Year', 'Description', 'Price NRS',  'Available Qty']
        c = 20
        print("\n1. To View first All Books") #idea: Make sorting here by alphabetically , price...
        print(f"2. To View first {c} Books")
        print(f"3. To View Last {c} Books")
        print("4. Exit ")
        
        user_input = int(input("\nEnter your choice: "))
        print("\n Books: ")
        print()


        if role == "Admin":
            #prints all header for admin
            df = pd.read_csv(path)
        elif role == "User":
            #prints only the selected header for users
            df = pd.read_csv(path, usecols= columns)

        if user_input ==1:
            print(df)
        elif user_input ==2:
            print(df.head(c))
        elif user_input ==3:
            print(df.tail(c))
        elif user_input == 4:
            exit()
        else:
            print("Select from the given options!!!")

    except pd.errors.EmptyDataError:
        print(f"\n {path} file is empty")

    except Exception as e:
        print(f"\n Undexpected error: {e}")

def add_book():
    book_path = r"LibraryManagement\LibM1\books.csv"
    file_exists = v.check_file_existance(book_path)
    fields = ['B_ID', 'Title', 'ISBN', 'Author', 'Published Year', 'Description', 'Price NRS', 'Total Qty', 'Available Qty', "Inclusion Date"]
    
    if not file_exists:
        v.add_csv_header(book_path, fields)

    if file_exists:
        with open (book_path, mode= "a+", newline="") as book_file:
            b_write = csv.DictWriter(book_file, fieldnames=fields)

            b_id = v.valid_id(book_path,"B_ID")
            title = v.validate_title()
            isbn = v.validate_isbn()
            author = v.validate_auhor(title)
            published_y = v.validate_year(title)
            description = v.validate_description(title)
            price = v.validate_price(title)
            t_qty = v.validate_total_qty()
            ava_qty = v.validate_available_qty(t_qty)
            i_date= v.curr_date_time()

            try:
                new_book = {
                    "B_ID": b_id + 1,
                    "Title": title,
                    "ISBN": isbn,
                    "Author": author,
                    "Published Year": published_y,
                    "Description": description,
                    "Price NRS": price,
                    "Total Qty": t_qty,
                    "Available Qty": ava_qty,
                    "Inclusion Date": i_date
                }
                b_write.writerow(new_book)
                print(f"\n \"{title}\" book successfully added.")
            except ValueError:
                print(f"\n Adding Book Value Error: {ValueError}")
            except Exception as e:
                print(f"\n Adding Book Error: {e}")

def del_book():
    book_path = r"LibraryManagement\LibM1\books.csv"
    file_exists = v.check_file_existance(book_path)
    while file_exists:
        try:
            choice = m.del_book_menu()
            df = pd.read_csv(book_path)
            if choice ==1:
                del_id = int(input("\nBook ID to delete: "))

                if del_id not in df["B_ID"].values:
                    print (f"\nBook ID {del_id} does not exists!!!")
                else:
                    df = df[df["B_ID"]!=del_id]
                    df.to_csv(book_path, index=False)
                    print(f"\nID {del_id} book deleted successfully")

            elif choice ==2:
                del_isbn = int(input("\nBook ISBN to delete: "))

                if del_isbn not in df["ISBN"].values:
                    print (f"\nISBN {del_isbn} book does not exists!!!")
                else:
                    df = df[df["ISBN"]!=del_isbn]
                    df.to_csv(book_path, index= False)
                    print(f"\nISBN {del_isbn} book deleted successfully")

            elif choice ==3:
                exit()
            else:
                print("Select from the given options!!!")
            
        except ValueError as ve: 
            print(f"\n Deleter User Data Type Error: {ve}")
        except Exception as e:
            print(f"\n Delete Error: {e}")
