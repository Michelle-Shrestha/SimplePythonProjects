import os, csv
def user_db_headname():
    fields = ["ID", "Role", "Username", "Password", "Status"]
    filename = r"LibraryManagement\LibM1\user_db.csv"
    file_exist = os.path.exists(filename)
    with open(filename, 'a',newline='') as userdb:
        write = csv.DictWriter(userdb, fieldnames= fields)
        if not file_exist:
            write.writeheader()
        else:
            print("\nuser_db.csv file already exists")

user_db_headname()

def books_csv_headname():
    csv_books_path = r"LibraryManagement\LibM1\books.csv"
    fieldname = ['B_ID', 'Title', 'Author', 'Published Year', 'DOI', 'Price', 'Total Qty','Available Qty' "Inclusion Date"]
    file_exist = os.path.exists(csv_books_path)
    with open (csv_books_path, mode= 'a', newline='') as book_file:
        write = csv.DictWriter(book_file, fieldnames= fieldname)
        if not file_exist:
            write.writeheader()
            print("\nHeader written to books.csv")
        else:
            print("\nBook.csv file already exists")

#books_csv_headname()

def add_csv_header(csv_path, fieldname):
    file_exist = os.path.exists(csv_path)
    with open(csv_path,mode='a', newline="") as csv_file:
        write = csv.DictWriter(csv_file,fieldnames=fieldname)
        if not file_exist:
            write.writeheader()
            print(f"\nHeader Written to {csv_path}")
        else:
            print(f"\n{csv_path} Header already Exists")

csv_books_path = r"LibraryManagement\LibM1\books.csv"
fieldname = ['B_ID', 'Title', 'Author', 'Published Year', 'DOI', 'Price', 'Total Qty','Available Qty', "Inclusion Date"]

add_csv_header(csv_books_path, fieldname)