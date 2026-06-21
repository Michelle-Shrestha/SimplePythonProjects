import os, csv, pandas as pd
from datetime import datetime as dt, date as d
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
    curr = dt.now().strftime(r"%Y-%m-%d %a")
    return(curr)

def int_check(u_input):
    if u_input.isalpha() and u_input.upper()!= "Q":
        print(f"\n Invalid Input!!!")
    elif u_input.isdigit():
        return int(u_input)
    
def float_check(u_input):
    if u_input.isalpha() and u_input.upper()!= "Q":
        print(f"\n Invalid Input!!!")
    elif u_input.isdigit():
        return float(u_input)
    
def breaking(u_input):
    if u_input.capitalize() == "Q":
        print("Exiting")
        return False
    else:
        return True
        


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
                    username = input("\nEdit the username: ").title()
                else:
                    username = input("\nEnter the new username: ").title()

                if not username:
                    raise ValueError("Username cannot be empty!!!")
                running = breaking(username)
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
  

def validate_password(running = True):
    while running:
        try:
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
def edit_uid(path, header, column, uid):
    new_id= []
    with open (path, mode= "r") as r_files:
        read = csv.DictReader(r_files)
        for row in read:
            if int(row[column]) == uid:
                edited = valid_id(path, column, edit = True)
                row["U_ID"]= edited
                new_id.append(row)
    return new_id

                

#path = r"LibraryManagement\LibM1\user_db.csv"
#header = ["U_ID", "Username","Role", "Password", "Status", "Created Date"]
#column = "U_ID"
#a=  edit_uid(path,header, column, 1001)
#print(a)


#------------------ User Search feature


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
            print(f"\n Error is {e}")


def enter_isbn(edit= False, running = True):
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

            if isbn.isdigit() and length!= 13:
                print("\n Invalid ISBN length")

            isbn = int_check(isbn) #returns the input as int datatype
            if isbn:
                return isbn

        except Exception as e:
            print(f"\n ISBN Error: {e}")

def validate_isbn():
    book_path = r"LibraryManagement\LibM1\books.csv"
    file_exists = check_file_existance(book_path)
    if file_exists:
        
            try:
                isbn = enter_isbn()
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
                print(f"\n Error is {e}")


def validate_auhor(title, edit = False):
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
            print(f"\n Error is {e}")

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
            print(f"\n Error is {e}")



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
            print(f"\n Error is {e}")


def validate_description(title, edit = False):
        try:
            if edit == True:
                description = input(f"\nEdit the book \n\"{title}\" description: ").strip().capitalize()
            else:
                description = input(f"\n\"{title}\" Book Description: ").strip().capitalize()

            breaking(description)

            if not description:
                return "Description not available"
            return description
        except Exception as e:
            print(f"\n Error is {e}")

#------------------- Book Edit Feature 

#------------------ Book Search feature

