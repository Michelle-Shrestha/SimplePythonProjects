import os, csv, pandas as pd
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
        print(f"{path} CSV file doesnot exists")
        return False
    return True

def admin_dashboard(): 
    print ("------ Admin Dashboard ------------")
    print("1. Books List")
    print("2. Edit book list")
    print("1. Add New Book")
    print("1. Add New Users")
    print("1. Edit Users List")


def add_book_draft():
    while True:
        

        book_path = r"LibraryManagement\LibM1\books.csv"
        fileexists = os.path.exists(book_path)
        if not fileexists:
            print(f"\n{book_path} FILE DOES NOT EXIST!!!")
            print(f"Creating a new file")

        with open(book_path, mode="a+", newline="") as book:
            book.seek(0) #setting pointer to start reading from the beginning
            fields = ['B_ID', 'Title', 'Author', 'Published Year', 'DOI', 'Price', 'Total Qty', "Inclusion Date"]
            b_writer = csv.DictWriter(book, fieldnames=fields)
            b_read = csv.DictReader(book)
           
            title = input("\nEnter the Title: ").strip()
            i_date = d.today().strftime("%Y-%m-%d") # strftime is used for formatting date in proper order
            doi = input("Enter the DOI: ").strip()

            #Checking whether the book alreay exists or not
            exist = False
            try:
                rows = list(b_read) # for storing rows and not exhausting reading b list
                b_id = rows+1 
                for row in rows:
                    if row['DOI']== doi:
                        print(f"\nDOI {doi} Book already Exists")
                        exist = True
                        continue
            except Exception as e:
                print(f"DOI Error: {e}")
            
            if not exist:
                author = input("Enter the author name: ").strip()
                
                try:
                    published_year = int(input("Enter the published year: "))
                    valid= validate_year(published_year)
                    if valid:
                        price = int(input("Enter the book price: "))
                        total_qty = int(input("Enter the total quantity: "))
                    else:
                        print("Invalid Year")
                except Exception as e:
                    print(f"Error: {e}")
                 

                new_book = {
                    "B_ID": b_id,
                    "Title": title,
                    "Author": author,
                    "Published Year": published_year,
                    "DOI": doi,
                    "Price": price,
                    "Total Qty": total_qty,
                    "Inclusion Date": i_date
                }
                b_writer.writerow(new_book)
                print(f"\n{title} Book successfully added!!!")
                return new_book


#new_book=add_book()

df = pd.read_csv(r"LibraryManagement\LibM1\user_db.csv")
print(df)

def validatee_year():
    while True:
        try:
            year = int(input("\nEnter the published year: "))
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
            
     
        
def validate_year(year):
    curr_year = dt.now().year
    if curr_year<year or year<1400:
        print("\n Invalid Year")
        return False
    return True

def validatee_price(title, curr_s = "NRS"):
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

valid = validatee_price("into the wild")
print(valid)
  
def validate_price(price, curr_s = "NRS"):
    max_price = 1000000
    min_price = 50
    curr_symbol = curr_s
    if max_price<price:
        print (f"\n Price must be less than {curr_symbol} {max_price + 1}")
        return False
    
    elif price <min_price:
        print(f"\n Price must be more than {curr_symbol} {min_price - 1}")
        return False
    
    return True

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
            qty= int(input("\nEnter the total quantity: "))
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

valid = validate_available_qty(100)
print(valid)


def add_book():
    book_path = r"LibraryManagement\LibM1\books.csv"
    file_exists = check_file_existance(book_path)
    if file_exists:
        with open (book_path, mode= "a+", newline="") as book_file:
            print(file_exists)

add_book()