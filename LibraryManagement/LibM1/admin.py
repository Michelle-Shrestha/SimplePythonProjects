import os, csv, pandas as pd 
import validation as v, menus as m #importing local py files


def user_details(user_path,running= True):
    file_exists = v.check_file_existance(user_path)
    c = 10
    if file_exists:
        while running:
            print("\n1. To View first All User")
            print(f"3. To View Last {c} user")
            print(f"4. Exit")
            
            try:
                user_input = int(input("\nEnter your choice: "))
                print("\n Users: ")
                print()
                
                df = pd.read_csv(user_path)
                if user_input ==1:
                    print(pd.DataFrame(df))
                elif user_input ==2:
                    print(df.head(c))
                elif user_input ==3:
                    print(df.tail(c))
                elif user_input==4:
                    break
                else:
                    print("Select from the given options!!!")
            except pd.errors.EmptyDataError:
                print(f"\n {user_path} file is empty")

            except Exception as e:
                print(f"\n Undexpected error: {e}")


def add_user(user_path):
    file_exists = v.check_file_existance(user_path)
    fields = ["U_ID", "Username","Role", "Password", "Status", "Created Date"]
    if not file_exists:
        v.add_csv_header(user_path, fields)
    running = True
    if file_exists:
        while running:
            user_input= input("\nPress Y  to be sure to add user Else press Q: ").capitalize()
            running = v.breaking(user_input)
            if user_input == 'Y':
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
            else: 
                print("Please enter Y to be sure")
         
def delete_users(user_path, m_running = True):
    file_exists = v.check_file_existance(user_path)
    if file_exists:
        while  m_running:
                try:
                    del_id= input("\nUser ID to delete: ").upper()
                    if not del_id:
                        raise ValueError ("Please Enter rhe User ID to Delete")
                    m_running = v.breaking(del_id)
                    df = pd.read_csv(user_path)
                    del_id = v.int_check(del_id)
                    if del_id:
                        try:
                            
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

def edit_users(user_path, m_running = True):
    file_exists = v.check_file_existance(user_path)
    if file_exists:
        id_type_Header = "U_ID"
        id = v.check_uid(user_path, id_type_Header)
        if id:
            while True:
                try:
                    m.edit_user()
                    choice = int(input("\nEnter your choice: "))
                    if choice ==1:
                        v.edit_username(user_path, id_type_Header,id)
                    elif choice ==2:
                        v.edit_role(user_path, id_type_Header,id)
                    elif choice ==3:
                        v.edit_status(user_path, id_type_Header,id)
                    elif choice ==4:
                        v.edit_password(user_path, id_type_Header,id)
                    elif choice==5:
                        v.view_row(user_path, id_type_Header,id)
                    elif choice==6:
                        print("\n Going Back...")
                        break
                    else:
                        print("\n Select from the given option!!!")
                        

                except ValueError as ve:
                    print(f"\n Edit User Value Error: {ve}")
                except Exception as e:
                    print(f"\n Edit User Error: {e}")

def user_crud(user_path, m_running = True):
    while m_running:
        try:
            m.user_crud_menu()
            user_input = int(input("\nEnter your choice: "))
            if user_input ==1:
                add_user(user_path)
            elif user_input==2:
                edit_users(user_path)
            elif user_input ==3:
                delete_users(user_path)
            elif user_input ==4:
                break
            else:
                print("\nSelect from the given option")

        except Exception as e:
            print(f"\n User CRUD Error: {e}")

def user_search(user_path, m_running= True):
    file_exists = v.check_file_existance(user_path)
    id_header = "U_ID"
    if file_exists:
        while m_running:
            try:
                m.search_user_menu()
                user_input = int(input("\nEnter your choice: "))
                if user_input ==1:
                    v.by_id(user_path, id_header)
                elif user_input==2:
                    print("HEHE")
                elif user_input ==6:
                    break
                else:
                    print("\nSelect from the given option")

            except Exception as e:
                print(f"\n Search Error: {e}")

# ------------------------------------------------------------------ Book ------------------------------------------------------------------------------------

def book_details(path,role="User", running=True):
    file_exists = v.check_file_existance(path)
    if file_exists:
        while running:
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
                    break
                else:
                    print("Select from the given options!!!")

            except pd.errors.EmptyDataError:
                print(f"\n {path} file is empty")

            except Exception as e:
                print(f"\n Undexpected error: {e}")

def add_book(book_path):
    file_exists = v.check_file_existance(book_path)
    fields = ['B_ID', 'Title', 'ISBN', 'Author', 'Published Year', 'Description', 'Price NRS', 'Total Qty', 'Available Qty', "Inclusion Date"]
    
    if not file_exists:
        v.add_csv_header(book_path, fields)

    running = True
    if file_exists:
        while running:
            user_input= input("\nPress Y  to be sure to add book Else press Q: ").capitalize()
            running = v.breaking(user_input)
            if user_input == 'Y':
                with open (book_path, mode= "a+", newline="") as book_file:
                    b_write = csv.DictWriter(book_file, fieldnames=fields)

                    b_id = v.valid_id(book_path,"B_ID")
                    title = v.validate_title()
                    isbn = v.validate_isbn()
                    author = v.validate_author(title)
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

def delete_book(book_path, m_runninng =True):
    file_exists = v.check_file_existance(book_path)
    if file_exists:
        while m_runninng:
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
                    break
                else:
                    print("Select from the given options!!!")
                
            except ValueError as ve: 
                print(f"\n Deleter User Data Type Error: {ve}")
            except Exception as e:
                print(f"\n Delete Error: {e}")

def edit_books(book_path):
    file_exists = v.check_file_existance(book_path)

    if file_exists:
        id_type_Header = "B_ID"
        id = v.check_uid(book_path, id_type_Header)

        with open (book_path, mode="r") as read_file:
            reader = csv.DictReader(read_file)
            for row in reader:
                if int(row[id_type_Header])== id:
                    title = row["Title"]
                    total_qty= row["Total Qty"]
        if id:
            while True:
                try:
                    m.edit_book()
                    choice = int(input("\nEnter your choice: "))
                    
                    if choice ==1:
                        v.edit_title(book_path, id_type_Header,id)
                    elif choice ==2:
                        v.edit_isbn(book_path, id_type_Header,id)
                    elif choice ==3:
                        v.edit_author(book_path, id_type_Header,id,title)
                    elif choice ==4:
                        v.edit_pyear(book_path, id_type_Header,id,title)
                    elif choice ==5:
                        v.edit_description(book_path, id_type_Header,id,title)
                    elif choice ==6:
                        v.edit_price(book_path, id_type_Header,id,title)
                    elif choice ==7:
                        v.edit_t_qty(book_path, id_type_Header,id)
                    elif choice ==8:
                        v.edit_a_qty(book_path, id_type_Header,id,total_qty)
                    elif choice==9:
                        v.view_row(book_path, id_type_Header,id)
                    elif choice ==10:
                        print("\n Going Back...")
                        break
                    else:
                        print("\n Select from the given option!!!")

                except ValueError as ve:
                    print(f"\n Edit User Value Error: {ve}")
                except Exception as e:
                    print(f"\n Edit User Error: {e}")

def book_crud(book_path, u_running = True):
    while u_running:
        try:
            m.book_crud_menu()
            user_input = int(input("\nEnter your choice: "))
            if user_input ==1:
                add_book(book_path)
            elif user_input==2:
                edit_books(book_path)
            elif user_input ==3:
                delete_book(book_path)
            elif user_input ==4:
                break
            else:
                print("\nSelect from the given option")

        except Exception as e:
            print(f"\n Book CRUD Error: {e}")

def book_search(book_path, m_running= True):
    file_exists = v.check_file_existance(book_path)
    id_header = "B_ID"
    if file_exists:
        while m_running:
            try:
                m.search_book_menu(role ="Admin")
                user_input = int(input("\nEnter your choice: "))
                if user_input ==1:
                    v.by_id(book_path, id_header)
                elif user_input==2:
                    print("HEHE")
                elif user_input ==6:
                    break
                else:
                    print("\nSelect from the given option")

            except Exception as e:
                print(f"\n Search Error: {e}")
path = r"LibraryManagement\LibM1\books.csv"
book_search(path)

def main_func(role="Admin",is_running = True):
    book_path = r"LibraryManagement\LibM1\books.csv"
    user_path = r"LibraryManagement\LibM1\user_db.csv"
    while is_running:
        try:
            m.admin_dashboard()
            user_choice = int(input("Enter your choice: "))
            if user_choice==1:
                user_details(user_path)

            elif user_choice==2:
                book_details(book_path, role)

            elif user_choice==3:
                user_crud(user_path)

            elif user_choice==4:
                book_crud(book_path)

            elif user_choice==8:
                print("\nThank you for using <3")
                break
            else:
                print("Please Select from the given Options!!!")

        except Exception as e:
            print(f"ERROR: {e}")
