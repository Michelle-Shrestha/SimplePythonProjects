import os, csv
from datetime import datetime as dt, date as d
import time as t

def add_csv_header(csv_path, field):
    file_exist = os.path.exists(csv_path)
    with open (csv_path, mode= "w", newline="") as csv_file:
        write = csv.DictWriter(csv_file, fieldnames=field)
        if not file_exist:
            write.writeheader()
            print(f"Header Successfully Written in {csv_file}")
        else:
            print(f"{csv_path} Already Exists")

def check_file_existance(path):
    file_exist = os.path.exists(path)
    if not file_exist:
        print(f"{path} file doesnot exists")
        return False
    return True

# -------------------------------------- Validation --------------------------------

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
            print("Enter a valid ISBN")
        
        elif length!= 13:
            print("Enter valid ISBN length")
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
                        if row["ISBN"] == isbn:
                            print(f"Given book already exists!!!")
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
        except ValueError:
            print("\n Enter valid integer!!!")
            

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
        except ValueError:
            print(f"\n Enter Valid Input!!!")

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
        except ValueError:
            print(f"\n Error is {ValueError}")
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
        except ValueError:
            print(f"\n Error is {ValueError}")
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
            return description
        except Exception as e:
            print(f"\n Error is {e}")

