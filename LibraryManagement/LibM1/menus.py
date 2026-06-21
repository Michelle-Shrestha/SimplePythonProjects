# MAIN admin Menu
def admin_dashboard(): 
    print ("\n------ Admin Dashboard ------------")
    print("1. Books List ")
    print("2. User Database ")
    print("3. User Sub Menu ")
    print("4. Book Sub Menu ")
    print("5. Search User ")
    print("6. Search Book ")
    print("7. Borrowed Book ")
    print("8. Books Sold ")
    print("9. Exit ") 


#----------------- Users------------------
def user_crud_menu():
    print("\n----------------")
    print("1. Add User ")
    print("2. Edit User ")
    print("3. Delete User ")
    print("4. Exit ")

def edit_user():
    print("\n---- Edit -------")
    print("1. User ID ")
    print("2. Username ")
    print("3. Role ")
    print("4. Status ")
    print("5. Exit")

def view_menu():
    print("\n--------- Search ---------")
    print("1. ID ")
    print("2. Username ")
    print("3. Role")
    print("4. Created Date ")
    print("5. Status ")
    print("6. Exit")
    


#--------------- BOOKS ---------------
def book_crud_menu():
    print("\n----------------")
    print("1. Add Book ")
    print("2. Edit Book ")
    print("3. Delete Book ")
    print("4. Exit")

def edit_book():
    print("\n----------- Edit ----------")
    print("1. Book ID ")
    print("2. Title ")
    print("3. ISBN ")
    print("4. Author ")
    print("5. Published Year ")
    print("6. Description ")
    print("7. Price ")
    print("8. Total Quantity")
    print("9. Available Quantity ")
    print("10. Exit")


def search_book_menu(role):
    print("\n--------- Search ---------")
    print("1. Book ID")
    print("2. Title ")
    print("3. ISBN ")
    print("4. Author ")
    print("5. Published Year ")
    print("6. Price ")
    print("7. Available Qutantity")
    if role == "Admin":
        print("8. Total Quantity ")
        print("9. Inclusion Date")
        print("10. Exit ")
    if role == "User":
        print("8. Exit ")

def del_book_menu():
    try:
        print("\n---Delete Option--- ")
        print("1. Delete by ID")
        print("2. Delete by ISBN")
        print("3. Exit")

        choice = int(input("\nChoose Option: "))
        if choice:
            return choice

    except ValueError as ve:
        print(f"\n Delete Value Error: {ve}")