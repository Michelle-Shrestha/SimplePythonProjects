import os, csv, pandas as pd, validation as v


def admin_dashboard(): 
    print ("------ Admin Dashboard ------------")
    print("1. Books List")
    print("2. User Database")
    print("1. Add New Book")
    print("1. Add New Users")
    print("2. Edit book list")
    print("1. Edit Users List")

# fields = ['B_ID', 'Title', 'ISBN', 'Author', 'Published Year', 'Price', 'Total Qty', "Inclusion Date"]

df = pd.read_csv(r"LibraryManagement\LibM1\user_db.csv")
print(df)


def add_book():
    book_path = r"LibraryManagement\LibM1\books.csv"
    file_exists = v.check_file_existance(book_path)
    fields = ['B_ID', 'Title', 'ISBN', 'Author', 'Published Year', 'Description', 'Price NRS', 'Total Qty', 'Available Qty', "Inclusion Date"]
    
    if not file_exists:
        v.add_csv_header(book_path, fields)

    if file_exists:
        with open (book_path, mode= "a+", newline="") as book_file:
            book_file.seek(0)
            b_read = csv.DictReader(book_file)
            b_write = csv.DictWriter(book_file, fieldnames=fields)
            rows = list(b_read)
            b_id = len(rows)+1
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
                    "B_ID": b_id,
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

    
#1001,Into The Wild,9780385486804,Jon Krakauer,1996,800.0,10,10
add_book()
df =pd.read_csv(r"LibraryManagement\LibM1\books.csv")
print(df)