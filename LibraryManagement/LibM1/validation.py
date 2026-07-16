import os, csv, pandas as pd
from datetime import datetime as dt, date as d, timedelta
import time as t
import hashlib

def add_csv_header(csv_path, field):
    file_exist = os.path.exists(csv_path)
    with open (csv_path, mode= "w", newline="") as csv_file:
        write = csv.DictWriter(csv_file, fieldnames=field)
        if not file_exist:
            write.writeheader()
            print(f"\nHeader Successfully Written in {csv_file}")
        else:
            print(f"\n{csv_path} Already Exists")

def check_file_existance(path):
    file_exist = os.path.exists(path)
    if not file_exist:
        print(f"{path} file doesnot exists")
        return False
    return True

              
#--------------------------------------- BOTH ------------------------------------------------
def valid_id(path, column, edit = False):
        try:
            user_path = path
            file_exists = check_file_existance(user_path)
            last_row = None

            if edit == True:
                new_id = int(input("\nEdit the id: "))
                if not new_id:
                    raise ValueError("Please enter a valid id!!!")
                else:
                    return new_id


            if file_exists:
                with open (user_path, mode="r") as user_file:
                    id_read = csv.DictReader(user_file)
                    for row in id_read:
                        if row:
                            last_row = row
                    #or can also do:
                    # rows = list(id_read)
                    #last_row = rows[-1]
 
            if last_row:
                last_id = last_row[column]
                return int(last_id)
            
            return 0 # if there's nothing found returns 0

        except Exception as e:
            print(f"\n ID Error: {e}")
            # returning 0, to prevent int error while adding book id
            return 0


def curr_date_time():
    curr = dt.now().strftime(r"%Y-%m-%d")
    return(curr)

#if Q then breaks out from the loop
def breaking(u_input):
    if u_input.capitalize() == "Q":
        print("\nGoing Back")
        return False
    else:
        return True

#to return the input as int or floating value 
def int_check(u_input):
    if u_input.strip().isalpha() and u_input.upper()!= "Q":
        print(f"\n Invalid Input!!!")
    elif u_input.isdigit():
        return int(u_input)

def float_check(u_input): 
    if u_input.strip().isalpha() and u_input.upper()!= "Q":
        print(f"\n Invalid Input!!!")
    elif u_input.isdigit():
        return float(u_input)

#checks whether the user has given input value or not if not rasise error    
def empty_validation(user_input):
    if not user_input:
        raise ValueError ("Please dont leave it empty")
    
def check_uid_for_each(id_type, search = False, borrow = False):
    if id_type == "U_ID":
        if search==True:
            id = input("\nEnter the User ID to search: ").capitalize()
        elif borrow==True:
            id = input("\nEnter the User ID of borrowed book: ").capitalize()
        elif not search and not borrow:
            id = input("\nEnter the user id to edit: ").capitalize()
        empty_validation(id)
    if id_type == "B_ID":
        if search==True:
            id = input("\nEnter the Book ID to search: ").capitalize()
        elif borrow==True:
            id = input("\nEnter the Book ID: ").capitalize()
        elif not search and not borrow:
            id = input("\nEnter the book id to edit: ").capitalize()
        empty_validation(id)
    if id:     
        return id

#validates whether id exists or not and returns it
def check_uid(path, id_type, borrow_b= False, running = True):
    while running:
        try:
            id = check_uid_for_each(id_type, borrow= borrow_b)
            running = breaking(id)
            id = int_check(id)
            if id:
                with open(path, mode="r") as read_files:
                    id_read = csv.DictReader(read_files)
                    id_found = False
                    for row in id_read:
                        if int(row[id_type]) ==id:
                            id_found = True
                    if id_found:
                        return id
                    else: 
                        if id_type == "U_ID":
                            print(f"\nUser ID {id} not found!!!")
                        if id_type == "B_ID":
                            print(f"\nBook ID {id} not found!!!")
        except Exception as e:
            print(f"\n ID error: {e}")  

#Edit the cols (takes param: csv file, id header whether of book or col, uni id no, col header of changing variable, and the replacing val)
def edit_value(file_path, id_type , id_no, column, new_val, extend_date = False):
    file_exists = check_file_existance(file_path)
    if file_exists:
        try:
            with open(file_path, mode= "r") as read_file:
                reader = csv.DictReader(read_file)
                rows = []
                field = reader.fieldnames #reading fields directly from file
                #Checks whether the columns exists or not
                if column not in field:
                    raise ValueError (f"\nColumn {column} does not exist in CSV")
                
                for row in reader:
                    if int(row[id_type])== id_no:
                        if str(row[column])==str(new_val):
                            print("\nThe new value is same as old ones!!!")
                        else:
                            if new_val == False:
                                print("\nEnter Valid Input!!")
                            elif new_val == None:
                                None
                            else:
                                row[column] = new_val
                                if extend_date:
                                    print(f"\nSuccessfully extended the book deadline till \"{new_val}\" ")
                                else:
                                    print(f"\nSuccessfully changed to new value \"{new_val}\" ")
                    rows.append(row)

            with open(file_path, mode="w", newline="") as write_file:
                writer = csv.DictWriter(write_file, fieldnames=field)
                writer.writeheader()

                for row in rows:
                    writer.writerow(row)

        except Exception as e:
            print(f"Edit Error: {e}")  

def view_row (path, id_type, id,return_csv = False):
    rows = []
    with open (path, mode="r") as read_file:
        reader = csv.DictReader(read_file)

        for row in reader:
            if int(row[id_type])== id:
                rows.append(row)
    df = pd.DataFrame(rows)
    if id_type == "U_ID" and return_csv == False:
        fields =["U_ID", "Username","Role", "Status", "Created Date"] 
        df = df[fields]
    elif id_type =="U_ID" and return_csv==True:
        csv_fields = reader.fieldnames
        df=df[csv_fields]
    print(df.to_string(index=False))

#for search 
def by_id(path, col_header, borrow_return = False,running= True,):
    file_exists = check_file_existance(path)
    if file_exists:
        while running:
            rows=[]
            found  = False
            try: 
                search_id =check_uid_for_each(col_header, search=True)
                running = breaking(search_id)
                search_id = int_check(search_id)

                if search_id:
                    with open (path, mode = "r") as read_file:
                        reading = csv.DictReader(read_file)

                        for read in reading:
                            if int(read[col_header])==search_id:
                                rows.append(read)
                                found = True

                        if not found:
                            if col_header == "U_ID":
                                print(f"\nUser ID {search_id} not found!!!")
                            elif col_header =="B_ID":
                                print(f"\nBook ID {search_id} not found!!!")

            except Exception as e:
                print(f"\n Search ID Error: {e}")
            if found:
                df = pd.DataFrame(rows)
                if col_header == "U_ID" and not borrow_return:
                    print(f"\nUser ID {search_id}: \n")
                    fields =["U_ID", "Username","Role", "Status", "Created Date"]
                    df = df[fields]
                    print(df.to_string())
                elif col_header == "U_ID" and borrow_return:
                    print(f"\nSearch Result: \n")
                    print(df.to_string())

                elif col_header =="B_ID":
                    print(f"\nBook ID {search_id}: \n")
                    print(df.to_string())

def by_created_date(path, header, id_header, borrow =False, return_b =False, running = True):
    file_exists = check_file_existance(path)
    if file_exists:
        while running:
            try:
                search_date = input("\nEnter the search date in %Y-%m-%d format separated by space: ").split(" ")
                search_date = "-".join(search_date)
                if not search_date:
                    raise ValueError("Please dont leave it empty!!!")
                running = breaking(search_date)
                if search_date and search_date!="Q":
                    result = search_result(path, header, search_date)
                    if result:
                        df = pd.DataFrame(result)
                        if borrow and return_b:
                            print(f"\nBooks to be returned on: {search_date}\n")
                            print(df.to_string())
                        elif borrow:
                            print(f"\nBooks Borrowed on {search_date}: \n ")
                            print(df.to_string())
                        elif return_b:
                            print(f"\nBooks Returned on {search_date}:\n")
                            print(df.to_string())
                            
                        else:
                            if id_header =="U_ID":
                                fields =["U_ID", "Username","Role", "Status", "Created Date"]
                                df=df[fields]

                                print(f"\nUser's Created in {search_date}: \n")
                                print(df.to_string())

                            elif id_header=="B_ID":
                                print(f"\nBooks Created in {search_date}: \n")
                                print(df.to_string()) 

            except Exception as e:
                print(f"\n Created Date Error: {e}")

#returns the resulted rows
def search_result (user_path, header,  search_value):
    try:
        rows =[]
        found = False
        with open(user_path, mode= "r") as read_files:
            if search_value:
                reading = csv.DictReader(read_files)
                for read in reading:
                    if str(read[header])== str(search_value):
                        rows.append(read)
                        found = True
            #if not found and search_value.upper()!="Q":
            #    print(f"\"{search_value}\" not found!!!")
            if found:
                return rows

    except Exception as e:
        print("Search Result Error: {e}")

#---------------------------------------------------------------------------------------------
# -------------------------------------- Validation For Users --------------------------------

#---------------adding users
def validate_username(edit = False, running = True):
    db_path = r"LibraryManagement\LibM1\user_db.csv"
    while running:
        try:
            found = False
            with open (db_path, mode="r") as db_file:
                u_read = csv.DictReader(db_file)
                if edit == True:
                    username = input("\nEdit the username: ").title().strip()
                else:
                    username = input("\nEnter the new username: ").title().strip()

                if not username:
                    raise ValueError("Username cannot be empty!!!")
                running = breaking(username)
                #is not necessary
                for row in u_read:
                    if row["Username"].title() ==username:
                        found = True
                        print(f"\nUsername \"{username}\" Already Exists")
                        continue
            if not found:
                return username
        except Exception as e:
            print(f"\n Username error: {e}")

def valid_role(edit= False):
    print("\nRoles:")
    print("1. User")
    print("2. Admin")
    print("3. Exit ")
    while True:
        try:
            if edit == True:
                role_input = int(input("\nEdit the Role: "))
            else:
                role_input = int(input("\nSelect the Role: "))

            if role_input ==1:
                return "User"
            elif role_input ==2:
                return "Admin"
            elif role_input ==3:
                break
            else:
                print("\n Please select a role from the given option")
            
        except ValueError as ve:
            print(f"\n Role Error: {ve}") 

def validate_password(edit = False, running = True):
    while running:
        try:
            if edit == True:
                pw = input("\nEdit the Password: ")
            else:
                pw = input("\nEnter the new password: ")
            if not pw:
                raise ValueError("Please enter password")
            running = breaking(pw) # to forcefully exit


            if pw and pw.upper()!="Q":
                c_pw = input("\nRe enter to confirm the password: ")
                breaking(c_pw)
                if not c_pw:
                    raise ValueError("Please enter confirm password!!!")
                if c_pw:
                    if pw == c_pw:
                        #hashlib is used to secure the user password
                        #hexdigest to conver it into hexa
                        h_pw = hashlib.sha256(pw.encode()).hexdigest()
                        return h_pw
                    else:
                        print("\n Password doesnot match")

        except Exception as e:
            print(f"\n Password Error: {e}")

def valid_status(edit= False):
    print("\nStatus:")
    print("1. Active")
    print("2. Inactive")
    print("3. Exit")
    while True:
        try:
            if edit == True:
                status_input = int(input("\nEdit the Status: "))
            else:
                status_input = int(input("\nSelect the Status: "))

            if status_input ==1:
                return "Active"
            elif status_input ==2:
                return "Inactive"
            elif status_input ==3:
                break
            else:
                print("\n Please select the status from the given option")
            
        except ValueError as ve:
            print(f"\n Status Error: {ve}")

#------------------- User Edit Feature 
def edit_username(user_path, id_type, id):
    new_un = validate_username(edit=True)
    col = "Username"
    edit_value(user_path, id_type, id, col, new_un )

def edit_role(user_path, id_type, id):
    new_un = valid_role(edit=True)
    col = "Role"
    edit_value(user_path, id_type, id, col, new_un )

def edit_status(user_path, id_type, id):
    new_un = valid_status(edit=True)
    col = "Status"
    edit_value(user_path, id_type, id, col, new_un )

def edit_password(user_path, id_type, id):
    new_pw = validate_password(edit=True)
    col = "Status"
    edit_value(user_path, id_type, id, col, new_pw )

#path = r"LibraryManagement\LibM1\user_db.csv"
#header = ["U_ID", "Username","Role", "Password", "Status", "Created Date"]
#column = "U_ID"
#edit_status(path, column, 1003)
#a=  edit_uid(path,header, column, 1001)
#print(a)


#------)------------ User Search feature
def by_username(user_path, header, field, running = True):
    file_exists = check_file_existance(user_path)
    if file_exists:
        while running:
            try:
                username = input("\nEnter the username to search: ").title()
                if not username:
                    raise ValueError ("Please dont leave it empty!!!")
                running = breaking(username)
                if username and username!="Q":
                    result = search_result(user_path, header, username)
                    if result:
                        print(f"\n{username} data: \n")
                        df = pd.DataFrame(result)
                        df= df[field]
                        print(df.to_string())

                    if not result:
                        print(f"\nUsername: {username} not found!!")

            except Exception as e:
                print(f"\n Username Search Error: {e}")

def by_role(user_path, header, field,running=True):
    file_exists = check_file_existance(user_path)
    if file_exists:
        while running:
            try:
                role = input("\nEnter the role to search: ").title()
                if not role:
                    raise ValueError ("Please dont leave it empty!!!")
                running = breaking(role)
                if role and role!="Q":
                    result = search_result(user_path, header, role)

                    if result:
                        print(f"\n{role} Users: \n")
                        df = pd.DataFrame(result)
                        df= df[field]
                        print(df.to_string())
                    if not result:
                        print(f"\nRole: {role} not found!!")

            except Exception as e:
                print(f"\n Role Search Error: {e}")

def by_status(user_path, header, field,running=True):
    file_exists = check_file_existance(user_path)
    if file_exists:
        while running:
            try:
                status = input("\nEnter the status to search: ").title()
                if not status:
                    raise ValueError ("Please dont leave it empty!!!")
                running = breaking(status)
                if status and status!="Q":
                    result = search_result(user_path, header,status)
                    if result:
                        print(f"\n{status} Users: \n")
                        df = pd.DataFrame(result)
                        df= df[field]
                        print(df.to_string())
                    if not result:
                        print(f"\nStatus: {status} not found!!")

            except Exception as e:
                print(f"\n Status Search Error: {e}")
    

#---------------------------------------------------------------------------------------------
# -------------------------------------- Validation for Books --------------------------------

#adding books
def validate_title(edit= False,running = True):
    while running:
        try:
            if edit == True:
                title = input("\nEdit the book title: ").strip().title()
            else:
                title = input("\nEnter the book title: ").strip().title()
            
            running = breaking(title)

            if title: 
                return title
            elif not title:
                raise ValueError("Please enter the book title!!!")
            
        except Exception as e:
            print(f"\n Error: {e}")

def enter_isbn(edit, running = True):
    while running:
        try:
            if edit == True:
                    isbn = input(f"\nEdit the ISBN:  ").strip()
            else:
                isbn = input(f"\nEnter the ISBN:  ").strip()
            length = len(isbn)
            if not isbn:
                raise ValueError ("Please enter the books ISBN !!!")
  
            running=breaking(isbn)
            isbn = int_check(isbn) #returns the input as int datatype
            if isbn:
                if length!= 13:
                    print("\n Invalid ISBN length")    
                else:
                    return isbn

        except Exception as e:
            print(f"\n ISBN Error: {e}")

def validate_isbn(edit = False):
    book_path = r"LibraryManagement\LibM1\books.csv"
    file_exists = check_file_existance(book_path)
    if file_exists:
        
            try:
                isbn = enter_isbn(edit)
                with open(book_path, mode="r", newline="") as book_file:
                    read = csv.DictReader(book_file)
                    found = False
                    for row in read:
                        if row["ISBN"] == isbn: #checking if there's already the same isbn
                            print(f"\n Given isbn book already exists!!!")
                            found = True
                            break   
                    if not found:   
                        return(isbn)

            except Exception as e:
                print(f"\n Error: {e}")

def validate_author(title, edit = False):
        try:
            if edit == True:
                author = input(f"\nEdit the book \"{title}\" Author name: ").strip().title()
            else:
                author = input(f"\nEnter the book \"{title}\" Author name: ").strip().title()
            
            breaking(author)

            if not author:
                return "Unknown Author"
            return author
        except Exception as e:
            print(f"\n Error: {e}")

def validate_year(title, edit = False, running = True):
    while running:
        try:
            if edit == True:
                year = input(f"\nEdit the book \"{title}\" published year: ")
            else:
                year = input(f"\nEnter the book \"{title}\" published year: ")
                running = breaking(year)
            
            if not year:
                raise ValueError("Please enter the published year!!!")
            year = int_check(year)

            if year:
                curr_year = dt.now().year
                old_year = 1400
                if curr_year<year:
                    print(f"\n Invalid Year, It must be less than year {curr_year + 1 }")
                elif year<1400:
                    print(f"\n Invalid year, IT must be more than year {old_year - 1}")
                else:
                    return year

        except Exception as e:
            print(f"\n Year error: {e}")

def validate_description(title, edit = False):
        try:
            if edit == True:
                description = input(f"\nEdit the book \n\"{title}\" description: ").strip().capitalize()
            else:
                description = input(f"\n\"{title}\" Book Description: ").strip().capitalize()

            breaking(description)

            if not description:
                return "Description not available"
            else:
                return description
        except Exception as e:
            print(f"\n Error: {e}")

def validate_price(title, curr_s = "NRS", edit = False, running=True):
    while running:
        max_price = 1000000
        min_price = 50
        curr_symbol = curr_s
        try:
            if edit == True:
                price = input(f"\nEdit the book \"{title}\" price: ")
            else:
                price = input(f"\nEnter the book \"{title}\" price: ")
            running = breaking(price)

            if not price:
                raise ValueError("Please enter the book price!!!")
            price = float_check(price)

            if price:
                price = float(price)
                if max_price<price:
                    print (f"\n Price must be less than {curr_symbol} {max_price + 1}")
                
                elif price <min_price:
                    print(f"\n Price must be more than {curr_symbol} {min_price - 1}")
                else:
                    return price
            
        except Exception as e:
            print(f"\n Price error: {e}!!!")

def validate_total_qty(edit= False, running = True):
    while running:
        max_qty = 150
        min_qty = 1
        try:
            if edit == True:
                qty= input("\nEdit the total quantity: ")
            else:
                qty= input("\nEnter the total quantity: ")
            running=breaking(qty)
            if not qty:
                raise ValueError("Please enter the book's total quantity!!!")
            qty = int_check(qty)
            if qty:
                qty = int(qty)
                if max_qty < qty:
                    print (f"\n Can have upto {max_qty} quantity")
                
                elif qty<min_qty:
                    print(f"\n Atleast should have {min_qty} quantity")
                else:
                    return qty

        except Exception as e:
            print(f"\n Error: {e}")

def validate_available_qty(t_qty, edit = False, running = True):
    while running:
        max_qty = t_qty
        min_qty = 0
        try:
            if edit == True:
                qty= input("\nEdit the availalbe quantity: ")
            else:
                qty= input("\nEnter the available quantity: ")

            running=breaking(qty)
            if not qty:
                raise ValueError("Please enter the book's available quantity!!!")
            
            qty = int_check(qty)
            if qty:
                if max_qty < qty:
                    print (f"\n Must be less than  {max_qty +1} quantity")
                
                elif qty<min_qty:
                    print(f"\n Cant have negative quantity!!!")
                else:
                    return qty
            
        except Exception as e:
            print(f"\n Error: {e}")

#------------------- Book Edit Feature 

def edit_title(book_path, id_type, id):
    new_un = validate_title(edit=True)
    col = "Title"
    edit_value(book_path, id_type, id, col, new_un )

def edit_isbn(book_path, id_type, id):
    new_isbn = validate_isbn(edit=True)
    col = "ISBN"
    edit_value(book_path, id_type, id, col, new_isbn )

def edit_author(book_path, id_type, id,title):
    new_author= validate_author(title=title, edit=True)
    col = "Author"
    edit_value(book_path, id_type, id, col, new_author )

def edit_pyear(book_path, id_type, id,title):
    new_pub_year= validate_year(title=title, edit=True)
    col = "Published Year"
    edit_value(book_path, id_type, id, col, new_pub_year )

def edit_description(book_path, id_type, id,title):
    new_description= validate_description(title=title, edit=True)
    col = "Description"
    edit_value(book_path, id_type, id, col, new_description )

def edit_price(book_path, id_type, id,title):
    new_price= validate_price(title=title, edit=True)
    col = "Price NRS"
    edit_value(book_path, id_type, id, col, new_price )

def edit_t_qty(book_path, id_type, id):
    new_t_qty= validate_total_qty(edit=True)
    col = "Total Qty"
    edit_value(book_path, id_type, id, col, new_t_qty )

def edit_a_qty(book_path, id_type, id,t_qty):
    new_a_qty= validate_available_qty(t_qty,edit=True)
    col = "Available Qty"
    edit_value(book_path, id_type, id, col, new_a_qty )




#------------------ Book Search feature
def by_title(book_path,col_header,field, searching= True):
    file_exists = check_file_existance(book_path)
    if file_exists:
        while searching:
            try:
                title = input("\nEnter the title to search: ").title()
                searching = breaking(title)
                if not title:
                    raise ValueError("Please do not leave the title empty to search!!!")
                if title and title!="Q":
                    result = search_result(book_path, col_header, title)
                    if result:
                        print(f" \"{title}\" result:\n ")
                        df = pd.DataFrame(result)
                        df= df[field]
                        print(df.to_string())
                    if not result:
                        print(f"\nTitle: {title} not found")

                
            except Exception as e:
                print(f"\n Title Search Error: {e}")


def by_isbn(book_path, col_header, field, searching = True):
    file_exists = check_file_existance(book_path)
    if file_exists:
        while searching:
            try:
                isbn = input("\nEnter the isbn to search: ").title()
                searching = breaking(isbn)
                if not isbn:
                    raise ValueError("Please do not leave the isbn empty!!!")
                if len(isbn)!=13:
                    raise ValueError("Invalid ISBN Length!!!")
                isbn  = int_check(isbn)
                if isbn:
                    result = search_result(book_path, col_header, isbn)
                    if result:
                        print(f"\nISBN {isbn} result: \n")
                        df = pd.DataFrame(result)
                        df=df[field] 
                        print(df.to_string())
                    if not result:
                        print(f"\nISBN: {isbn} not found!!!")

            except Exception as e:
                print(f"\n ISBN Search Error: {e}")

def by_author(book_path, col_header, field, searching = True):
    file_exists = check_file_existance(book_path)
    if file_exists:
        while searching:
            try:
                author = input("\nEnter the author name to search: ").title()
                searching = breaking(author)
                if not author:
                    raise ValueError("Please do not leave the author name empty!!!")

                if author:
                    result = search_result(book_path, col_header, author)
                    if result:
                        print(f"\nAuthor {author} result: \n")
                        df = pd.DataFrame(result)
                        df=df[field] 
                        print(df.to_string())
                    if not result:
                        print(f"\nAuthor: {author} not found!!!")

            except Exception as e:
                print(f"\nAuthor Search Error: {e}")

def by_publishedY(book_path, col_header, field, searching = True):
    file_exists = check_file_existance(book_path)
    if file_exists:
        while searching:
            try:
                publishedY = input("\nEnter the isbn to search: ").title()
                searching = breaking(publishedY)
                if not publishedY:
                    raise ValueError("Please do not leave the year empty!!!")
                if len(publishedY)!=4:
                    raise ValueError("Invalid year Length!!!")
                publishedY  = int_check(publishedY)
                if publishedY:
                    result = search_result(book_path, col_header, publishedY)
                    if result:
                        print(f"\nBooks on Published Year {publishedY} result: \n")
                        df = pd.DataFrame(result)
                        df=df[field] 
                        print(df.to_string())
                    if not result:
                        print(f"\n Books onPublished Year: {publishedY} not found!!!")

            except Exception as e:
                print(f"\n Published Year Search Error: {e}")

def by_price(book_path, col_header, field, searching=True):
    file_exists = check_file_existance(book_path)
    if file_exists:
        while searching:
            try:
                price = input("\nEnter the price to search: ").title()
                searching = breaking(price)
                if not price:
                    raise ValueError("Please do not leave the price empty!!!")
                price  = float_check(price)
                if price:
                    result = search_result(book_path, col_header, price)
                    if result:
                        print(f"\nBooks of price: {price} result: \n")
                        df = pd.DataFrame(result)
                        df=df[field] 
                        print(df.to_string())
                    if not result:
                        print(f"\n Books of Price: {price} not found!!!")

            except Exception as e:
                print(f"\n Price  Search Error: {e}")

## ------------------ Borrow Book

def borrow_bID_title_qty(book_path, id_header, title_header, total_qty_h):
    book_file_exist = check_file_existance(book_path)
    if book_file_exist:
        book_id = check_uid(book_path, id_header, borrow_b= True)
        try:
                if book_id:
                    found = False
                    with  open (book_path, mode = "r") as book_file:
                        
                        id_read = csv.DictReader(book_file)
                        for row in id_read:
                            if int(row[id_header])==book_id: 
                                title = str(row[title_header])
                                t_qty = int(row[total_qty_h])
                                found = True
                                
                    if found:   
                        return book_id, title, t_qty
                    if not found:
                        print(f"\nBook ID {book_id} not found!!!")
                                
        except Exception as e:
            print(f"\n Borrow Book Error: {e}")


def borrow_uID_username(user_path, id_header, username_header, running = True):
    user_file_exist = check_file_existance(user_path)
    if user_file_exist:
        user_id = check_uid(user_path, id_header, borrow_b= True)
        if user_id:
            while running:
                try:
                    username = input("\nEnter the username: ").title().strip()
                    if not username:
                        raise ValueError ("Please dont leave it empty!!!")
                    running = breaking(username)
                    if username and username!="Q":
                        match = False
                        with open(user_path, mode="r") as user_file:
                            reading = csv.DictReader(user_file)
                            
                            for row in reading:
                                if int(row[id_header])== user_id:
                                    if row[username_header]==username:
                                        match = True
                            if match:
                                return user_id, username
                            else:
                                print(f"\nUsername {username} for ID {user_id} doesnot match!!!")

                except Exception as e:
                    print(f"\n Borrow User Error: {e}")

def available_qty_adjusting(book_path,b_header, book_id, ava_qty_header, total_qty, borrow_book= False, return_book= False):
    if book_id:
        try:
            with open (book_path, mode="r") as book_file:
                reading = csv.DictReader(book_file)
                rows=[]
                field = reading.fieldnames
                if ava_qty_header not in field:
                    raise ValueError(f"\nColumn {ava_qty_header} does not exist in CSV")
                for row in reading: 
                    if int(row[b_header]) ==book_id:
                        #if the book is still available
                        if borrow_book == True:
                            if int(row[ava_qty_header])>0:
                                row[ava_qty_header] = int(row[ava_qty_header])-1
                                print("\nSuccessfully Adjusted Available Quantity")
                            # if book is not available
                            else:
                                print(f"\nBook is out of stock!!!")

                        if return_book ==True:
                            if int(row[ava_qty_header])< total_qty:
                                row[ava_qty_header] = int(row[ava_qty_header])+1
                                print("\nSuccessfully Adjusted Available Quantity")
                            # if book is not available
                            else:
                                print(f"\nQutantity Mismatched!!!")

                    rows.append(row)

            with open (book_path, mode = "w", newline="") as write_file:
                writing = csv.DictWriter(write_file, field)
                writing.writeheader()

                for row in rows:
                    writing.writerow(row)

        except Exception as e:
            print(f"\n Qty Adjustment Error: {e}")

def return_date(curr_date, running = True):
    while running:
        #converting back to datetime
        curr_dt = dt.strptime(curr_date, "%Y-%m-%d")
        try:
            extend_weeks = input("\nHow many weeks to borrow: ")
            running = breaking(extend_weeks)
            extend_weeks = int_check(extend_weeks)
            if not extend_weeks:
                raise ValueError ("Please dont leave the borowing number of week empty!!!")
            else:
                #using time delta to find the date after a week
                return_d= curr_dt + timedelta(weeks=extend_weeks)
                #making it string
                return_d = dt.strftime(return_d, "%Y-%m-%d")
                if return_d:
                    return return_d
        except Exception as e:
            print(f"\n Return Date Error: {e}")

## ----------------------- Return BOOK
def returned_by_id_un(borrow_path, user_path,user_header, user_id_h, running = True):
    while running:
        try:
            not_valid = False
            user_found = False 
            is_borrowed = False
            user_id = None
            if user_header== "U_ID":
                user_valid = input("\nEnter the User ID: ")
                if not user_valid.isdigit():
                    print("\nInvalid User ID")
                    not_valid = True # checks for validating proper Integer ID
                
            elif user_header=="Username":
                user_valid = input("\nEnter the username: ").title().strip()

            if not user_valid:
                raise ValueError ("Please donot leave it empty!!!")
            elif user_valid and not not_valid:
                with open (user_path, mode="r") as user_file, \
                    open (borrow_path, mode="r") as borrow_file:
                    user_csv = csv.DictReader(user_file)
                    borrowed_csv = csv.DictReader(borrow_file)
                    for row in user_csv:
                        if str(user_valid) == str(row[user_header]): 
                            #if user exists in user csv file then only checks if user had borrowed book or not
                            user_id = int(row[user_id_h])
                            user_found = True
                            for borrowed in borrowed_csv:
                                if str(user_id) == (borrowed[user_id_h]): 
                                    is_borrowed = True
                                    break
                                    
                if user_found == False:
                    print(f"\nUser not found!!!")
                
                if user_found and is_borrowed == False:
                    print(f"\nUser has not recently borrowed book")
                
                else:
                    return is_borrowed, user_id

        except Exception as e:
            print(f"\nReturning Book Error: {e}")
        
def return_values(borrow_path, borrow_h, bid_h , bid, uid_h, uID,username_h):
        try:
            with open (borrow_path, mode="r") as read_file:
                reading = csv.DictReader(read_file)

                #checks if the book id is borrowed or not by the user
                for read in reading: 
                    if int(read[uid_h]) == int(uID):
                        if int(read[bid_h]) ==int(bid):
                            borrowed_id = int(read[borrow_h])
                            username = str(read[username_h])
                            return int(borrowed_id), username 
                        else:
                            print(f"\nUser ID {uID} has not borrowed the book with Book ID {bid}")
                            print(f"\nBooks borrowed by User ID {uID}: \n")
                            view_row(borrow_path, uid_h, uID, return_csv=True)
                            return None, None

        except Exception as e:
            print(f"\n Return Book Value Error: {e}")

def del_returnedbooks(borrowed_path, borrow_id_h, borrow_id):
    try:
        borrow_id = int(borrow_id)
        if not borrow_id:
            raise ValueError("Borrow ID is empty!!!")
        # Deleting the Returned Book from the borrowed csv to prevent duplicate data
        df = pd.read_csv(borrowed_path)
        if borrow_id:
            try:
                # checks whether the borrow id exists or not to delete it
                if borrow_id not in df[borrow_id_h].values:
                    print(f"\nBorrow ID: {borrow_id} does not exists")
                else:
                    #stores all the borrow id that is not del id
                    df = df[df[borrow_id_h]!=borrow_id]
                    df.to_csv(borrowed_path, index = False)
            except ValueError as ve:
                print(f"\n Deleter User Data Type Error: {ve}")

    except Exception as e:
        print(f"Delete Borrowed CSV ERROR: {e}")

##--------------------- Extend Book
def extend_user_book_id(borrow_path, borrow_h, bid_h,uid_h, username_h ):
    try: 
        with open(borrow_path, mode = "r") as borrow_file:
            borrowed= csv.DictReader(borrow_file)
            user_found = False
            book_found = False
            borrow_id = None
            user = input("Enter the User ID or Username: ")
            if not user:
                raise ValueError("Please donot leave it empty!!!")
            if user.isdigit():
                user = int(user)
            else:
                user = user.strip().title()

            for borrow in borrowed:
                    if user == int(borrow[uid_h]) or user == borrow[username_h]:
                        user_found = True
                        uID = int(borrow[uid_h])
                        book_id = int(input("Enter the Book ID: "))
                        if book_id == int(borrow[bid_h]):
                            book_found = True
                            borrow_id = int(borrow[borrow_h])
                            return borrow_id
        
            if not user_found:
                print(f"User not found")
            if user_found and not book_found:
                print(f"User have not borrowed this book!!!")
                view_row(borrow_path, uid_h, uID, return_csv=True)

    except Exception as e:
        print(f"Extend Book Error: {e}")

def extend_book_deadline(borrow_path, borrow_h, borrow_id,return_date_h):
        try:
            curr_date = dt.now().strftime("%Y-%m-%d")
            new_return_date = return_date(curr_date)
            #path, file uni id header and id number, col to be changed, changing value
            edit_value(borrow_path, borrow_h, borrow_id, return_date_h, new_return_date, extend_date= True)
        except Exception as e:
            print(f"\n Extending Deadling Error: {e}")

borrow_book_path= r"LibraryManagement\LibM1\borrowed_books.csv"
#extend_book_deadline(borrow_book_path, "B_ID", "U_ID", "Return Date")

#-------------------- Search Borrowed Books
def by_overdue(path, col_header, fields, searching= True):
    while searching:
        try:
            overdue_days = input("\nEnter the overdue days: ").title()
            searching = breaking(overdue_days)
            empty_validation(overdue_days)
            #overdue_days = int_check(overdue_days)
            if overdue_days and overdue_days!= "Q":
                result = search_result(path, col_header, overdue_days)

                if result:
                    print(f"\nBook overdue {overdue_days} days: \n")
                    df =pd.DataFrame(result)
                    df =df[fields]
                    print(df.to_string())
                else:
                    print(f"\n Overdue of {overdue_days} days not  found!!!")
        except Exception as e:
            print(f"Overdue days Search Error: {e}")


def overdue(return_date):
    try:
        #borr_d = dt.strptime(borrowed_date, "%Y-%m-%d")
        ret_d = dt.strptime(return_date, "%Y-%m-%d")
        curr_date = dt.now().strftime(r"%Y-%m-%d")
        curr_date = dt.strptime(curr_date, "%Y-%m-%d")
        overdue_days = (curr_date- ret_d).days #only returns the days in int data type
        if overdue_days < 0:
            return 0
        else:
            return overdue_days
    except Exception as e:
        print(f"\n Overdue Error: {e}")

#print(overdue("2026-6-9", "2026-6-7"))
    
def update_overdue(borrowed_path,return_d_h, overdue_h):
    try:
        rows= []
        with open (borrowed_path, mode = "r") as borrow_file:
            reading = csv.DictReader(borrow_file)
            fields = reading.fieldnames
            for row in reading:
                return_d = row[return_d_h]
                overdue_days = overdue(return_d)
                if overdue_days == None:
                    overdue_days = 0
                row[overdue_h] = overdue_days
                rows.append(row)
        
        with open(borrowed_path, mode="w", newline="") as write_file:
            writing = csv.DictWriter(write_file, fields)
            writing.writeheader()
            for row in rows:
                writing.writerow(row)
            print("\nSuccessfully Overdues Updated")

    except Exception as e:
        print(f"\n Overdue updating error: {e}")
#update_overdue(borrow_book_path, "Return Date", "Overdue")