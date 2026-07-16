# MAIN admin Menu
def admin_dashboard(): 
    print ("\n------ Admin Dashboard ------------")
    print("1. User Database ")
    print("2. Books List ")
    print("3. User Sub Menu ")
    print("4. Book Sub Menu ")
    print("5. Borrow and Return ")
    print("6. Search Operation ")
    print("7. Exit ") 
    print("----------------------------------\n")

def book_borrow_return_menu():
    try:
        print("\n-----Borrow and Return Books-----")
        print("1. View Borrowed Books ")
        print("2. View Returned Books ")
        print("3. Borrow Book ")
        print("4. Return Book ")
        print("5. Extend Deadline ")
        print("6. Update Overdue Days")
        print("7. Exit ")
        print("----------------------------\n")
        choice = input("\nChoose Option: ")
        if choice:
            return choice
        if not choice:
            raise ValueError ("Please donot leave it empty!!!")
    except ValueError as ve:
        print(f"\n Delete Value Error: {ve}")

def main_search_menu():
    try:
        print("\n-----Search OPERATION-----")
        print("1. User Search Menu")
        print("2. Book Search Menu ")
        print("3. Borrow Search Menu")
        print("4. Return Search Menu")
        print("5. Exit ")
        print("----------------------------\n")
        choice = input("\nChoose Option: ")
        if choice:
            return choice
        if not choice:
            raise ValueError ("Please donot leave it empty!!!")
    except ValueError as ve:
        print(f"\n Delete Value Error: {ve}")


#----------------- Users------------------
def user_crud_menu():
    print("\n-----USER CRUD OPERATION-----")
    print("      1. Add User ")
    print("      2. Edit User ")
    print("      3. Delete User ")
    print("      4. Exit ")
    print("----------------------------\n")

def edit_user():
    print("\n---- Edit -------")
    print("1. Username ")
    print("2. Role ")
    print("3. Status ")
    print("4. Password ")
    print("5. View User Data")
    print("6. Exit")
    print("----------------\n")

def search_user_menu():
    print("\n--------- Search ---------")
    print("1. ID ")
    print("2. Username ")
    print("3. Role ")
    print("4. Status ")
    print("5. Created Date ")
    print("6. Exit ")
    print("--------------------------\n")
    

#--------------- BOOKS ---------------
def book_crud_menu():
    print("\n-----BOOK CRUD OPERATIONS-----")
    print("      1. Add Book ")
    print("      2. Edit Book ")
    print("      3. Delete Book ")
    print("      4. Exit")
    print("-----------------------------\n")

def edit_book():
    print("\n----------- Edit ----------")
    print("1. Title ")
    print("2. ISBN ")
    print("3. Author ")
    print("4. Published Year ")
    print("5. Description ")
    print("6. Price ")
    print("7. Total Quantity")
    print("8. Available Quantity ")
    print("9. View Book Data")
    print("10. Exit")
    print("-------------------------\n")


def search_book_menu(role):
    print("\n--------- Search ---------")
    print("1. Book ID")
    print("2. Title ")
    print("3. ISBN ")
    print("4. Author ")
    print("5. Published Year ")
    print("6. Price ")
    if role == "Admin":
        print("7. Inclusion Date")
        print("8. Exit ")
    if role == "User":
        print("7. Exit ")
    print("-----------------------\n")

def del_book_menu():
    try:
        print("\n--- Delete Option --- ")
        print("1. Delete by ID")
        print("2. Delete by ISBN")
        print("3. Exit")
        print("-----------------\n")

        choice = int(input("\nChoose Option: "))
        if choice:
            return choice

    except ValueError as ve:
        print(f"\n Delete Value Error: {ve}")

#-------------------------------- Borrow and return -----------
def return_by():
    try:
        print("\n---- Return Option ---- ")
        print("1. Return by User ID")
        print("2. Return by Username")
        print("3. Exit")
        print("-----------------\n")

        choice = input("\nChoose Option: ")
        if not choice:
            raise ValueError ("Please dont leave it empty!!")
        else:
            return choice

    except ValueError as ve:
        print(f"\n Delete Value Error: {ve}")

def search_borrowed_menu():
    try:
        print("\n--------- Search ---------")
        print("1. User ID ")
        print("2. Username ")
        print("3. Book ID ")
        print("4. Title ")
        print("5. Borrowed Date ")
        print("6. Return Date ")
        print("7. Overdue Days")
        print("8. Exit ")
        print("--------------------------\n")
        choice = input("\nChoose Option: ")
        if not choice:
            raise ValueError ("Please dont leave it empty!!")
        else:
            return choice

    except ValueError as ve:
        print(f"\n Seach Borrow Book Error: {ve}")

def search_returned_menu():
    try:
        print("\n--------- Search ---------")
        print("1. User ID ")
        print("2. Username ")
        print("3. Book ID ")
        print("4. Title ")
        print("5. Returned Date ")
        print("6. Exit ")
        print("--------------------------\n")
        choice = input("\nChoose Option: ")
        if not choice:
            raise ValueError ("Please dont leave it empty!!")
        else:
            return choice

    except ValueError as ve:
        print(f"\n Search Return Book Error: {ve}")