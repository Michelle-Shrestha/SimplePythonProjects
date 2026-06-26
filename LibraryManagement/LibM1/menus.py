# MAIN admin Menu
def admin_dashboard(): 
    print ("\n------ Admin Dashboard ------------")
    print("1. User Database ")
    print("2. Books List ")
    print("3. User Sub Menu ")
    print("4. Book Sub Menu ")
    print("5. Search User ")
    print("6. Search Book ")
    print("7. Borrowed Book ")
    print("8. Return Book ")
    print("9. Exit ") 
    print("----------------------------------\n")


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
        print("\n---Delete Option--- ")
        print("1. Delete by ID")
        print("2. Delete by ISBN")
        print("3. Exit")
        print("-----------------\n")

        choice = int(input("\nChoose Option: "))
        if choice:
            return choice

    except ValueError as ve:
        print(f"\n Delete Value Error: {ve}")
