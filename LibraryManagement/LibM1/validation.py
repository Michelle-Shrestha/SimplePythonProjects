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
def valid_id(path, header):
        try:
            user_path = path
            file_exists = check_file_existance(user_path)
            last_row = None

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
                last_id = last_row[header]
                return int(last_id)
            
            return 0 # if there's nothing found returns 0

        except Exception as e:
            print(f"\n ID Error: {e}")
            # returning 0, to prevent int error while adding book id
            return 0

#---------------------------------------------------------------------------------------------
# -------------------------------------- Validation For Users --------------------------------


#adding users
def validate_username():
    db_path = r"LibraryManagement\LibM1\user_db.csv"
    while True:
        found = False
        with open (db_path, mode="r") as db_file:
            u_read = csv.DictReader(db_file)
            username = input("\nEnter the new username: ").title()
            for row in u_read:
                if row["Username"].title() ==username:
                    found = True
                    print(f"\nUsername \"{username}\" Already Exists")
                    continue
        if not found:
            return username
        
def valid_role():
    print("\nRoles:")
    print("1. User")
    print("2. Admin")
    while True:
        try:
            role_input = int(input("\nSelect the Role: "))

            if role_input ==1:
                return "User"
            elif role_input ==2:
                return "Admin"
            else:
                print("\n Please select a role from the given option")
            
        except ValueError as ve:
            print(f"\n Role Error: {ve}")
    
def validate_password():
    db_path = r"LibraryManagement\LibM1\user_db.csv"
    while True:
        same_pw = False
        with open(db_path, mode="r") as db_file:
            try:
                read = csv.DictReader(db_file)
                pw = input("\nEnter the new password: ")
                if not pw:
                    print("\n Please enter password")
                if pw:
                    c_pw = input("\nRe enter to confirm the password: ")
                    
                    if not c_pw:
                        print("\n Please enter confirm password")
                    if c_pw:
                        if pw == c_pw:
                            #hashlib is used to secure the user password
                            #hexdigest to conver it into hexa
                            h_pw = hashlib.sha256(pw.encode()).hexdigest()
                            return h_pw
                        else:
                            print("\n Password doesnot match")

            except Exception as e:
                print(f"\n PW Error: {e}")


def valid_status():
    print("\nStatus:")
    print("1. Active")
    print("2. Inactive")
    while True:
        try:
            role_input = int(input("\nSelect the Status: "))

            if role_input ==1:
                return "Active"
            elif role_input ==2:
                return "Inactive"
            else:
                print("\n Please select the status from the given option")
            
        except ValueError as ve:
            print(f"\n Status Error: {ve}")


#---------Search feature -----------------------


#---------------------------------------------------------------------------------------------
# -------------------------------------- Validation for Books --------------------------------

#adding books
def validate_title():
    while True: 
        try:
            print ("Type Q or q to exit")
            title = input("\nEnter the book title: ").strip().title()
            if title.upper() == "Q":
                exit()
            return title
        except Exception as e:
            print(f"\n Error is {e}")

def enter_isbn():
    while True:
        print("Type Q or q to exit")
        isbn = input(f"\nEnter the ISBN:  ").strip()
        length = len(isbn)
        if isbn.upper() == "Q":
            exit()
        if not isbn.isdigit():
            print("\n Invalid ISBN ")
        
        elif length!= 13:
            print("\n Invalid ISBN length")
        else:
            return isbn
   

def validate_isbn():
    book_path = r"LibraryManagement\LibM1\books.csv"
    file_exists = check_file_existance(book_path)
    if file_exists:
        while True:
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

def validate_auhor(title):
    while True: 
        try:
            print ("Type Q or q to exit")
            author = input(f"\nEnter the book \"{title}\" Author name: ").strip().title()
            if author.upper() == "Q":
                exit()
            if not author:
                return "Unknown Author"
            return author
        except Exception as e:
            print(f"\n Error is {e}")


def validate_year(title):
    while True:
        try:
            year = int(input(f"\nEnter the book \"{title}\" published year: "))
            curr_year = dt.now().year
            old_year = 1400
            if curr_year<year:
                print(f"\n Invalid Year, It must be less than year {curr_year + 1 }")
            elif year<1400:
                print(f"\n Invalid year, IT must be more than year {old_year - 1}")
            else:
                return year
        except ValueError as ve:
            print(f"\n Invalid integer: {ve}!!!")
            

def validate_price(title, curr_s = "NRS"):
    while True:
        max_price = 1000000
        min_price = 50
        curr_symbol = curr_s
        try:
            price = float(input(f"\nEnter the book \"{title}\" price: "))
            if max_price<price:
                print (f"\n Price must be less than {curr_symbol} {max_price + 1}")
            
            elif price <min_price:
                print(f"\n Price must be more than {curr_symbol} {min_price - 1}")
            else:
                return price
        except ValueError as ve:
            print(f"\n Inalid Input: {ve}!!!")

def validate_total_qty():
    while True:
    
        max_qty = 150
        min_qty = 1
        try:
            qty= int(input("\nEnter the total quantity: "))
            if max_qty < qty:
                print (f"\n Can have upto {max_qty} quantity")
            
            elif qty<min_qty:
                print(f"\n Atleast should have {min_qty} quantity")
            else:
                return qty
        except ValueError as ve:
            print(f"\n Error is {ve}")
        except Exception as e:
            print(f"\n Error is {e}")

def validate_available_qty(t_qty):
    while True:
    
        max_qty = t_qty
        min_qty = 0
        try:
            qty= int(input("\nEnter the available quantity: "))
            if max_qty < qty:
                print (f"\n Must be less than  {max_qty +1} quantity")
            
            elif qty<min_qty:
                print(f"\n Cant have negative quantity!!!")
            else:
                return qty
        except ValueError as ve:
            print(f"\n Error is {ve}")
        except Exception as e:
            print(f"\n Error is {e}")

def curr_date_time():
    curr = dt.now().strftime(r"%Y-%m-%d %a")
    return(curr)

def validate_description(title):
    while True: 
        try:
            print ("Type Q or q to exit")
            description = input(f"\n\"{title}\" Book Description: ").strip().capitalize()
            if description.upper() == "Q":
                exit()

            if not description:
                return "Description not available"
            return description
        except Exception as e:
            print(f"\n Error is {e}")


#-------- Search Book Feature ---------------------------



