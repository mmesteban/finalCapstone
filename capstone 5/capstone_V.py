# Wew will manage the database with sqLite3
import sqlite3

# CLASSES -------------------------------------------------------------------


# METHODS -------------------------------------------------------------------
def user_options_input(inputs_descriptions):
    # This method:
    # - Prints a list of options
    # - Receives an input by the user
    # - Validates it against a list --> If not correct, asks again
    # - Returns the option if in dictionary
    while(True):
        print("Please select an option:")
        for i in inputs_descriptions:
            print(f"'{i}' - {inputs_descriptions[i]}")
        # input
        choice = input("Enter here your choice: ")
        # if input not in i --> say we dont recognise input, continue while loop
        if choice not in inputs_descriptions:
            print("\n - ERROR: Input not recognised: please try again.\n")
            continue
        # else --> output the option chosen
        else:
            print(f"\n - Option selected: '{choice}'.\n")
            return choice


def input_validator(mode, message):
    # allows the user to input data. Checks will be done according to the mode selected. It will manage the exceptions
    while True:
        if mode == "int":
            try:
                user_input = int(input(f"Please enter an int {message}: "))
                break
            except ValueError:
                print("Oops! That was not a valid integer. Try again...")
        elif mode == "str":
            user_input = input(f"Please enter a string {message}: ")
            if len(user_input) >= 2:
                break
            else:
                print("Oops! Strings must be longer than 2 chars. Try again...")
        else:
            raise RuntimeError(
                "Mode of method input_validator is not recognised")
    return user_input


def add_new_book():
    #   ○ Add new books to the database
    while (True):
        print("Add new books to the catalogue")
        # input id
        _id = input_validator("int", "for the Book´s id")
        # input title
        _title = input_validator("str", "for the Book´s title")
        # input author
        _author = input_validator("str", "for the Book´s author")
        # input quantity
        _quantity = input_validator("int", "for the Book´s quantity")
        answer = input(
            f"\n:{_id}-{_title}-{_author}-{_quantity}\nIs this data correct?(y/n)    ").lower()
        if "y" in answer:
            break
        else:
            print("No problem, lets enter it again")
            continue
    # db query
    try:
        cursor.execute('''INSERT INTO books(id, title, author, quantity)VALUES(?, ?, ?,?)''',(_id, _title, _author, _quantity,))
    except:
        print("Error trying to add the entry. Try with another id")

    print("Book added!")
    print("---------------------------------")


def update_book():
    #   ○ Update book information                       -> Code method
    # retrieve a book id to change form user
    while (True):
        print("Update book data in the catalogue")
        # input id
        _id = input_validator("int", "for the Book´s id")
        # input title
        _title = input_validator("str", "for the Book´s title")
        # input author
        _author = input_validator("str", "for the Book´s author")
        # input quantity
        _quantity = input_validator("int", "for the Book´s quantity")
        answer = input(
            f"\n:{_id}-{_title}-{_author}-{_quantity}\nIs this data correct?(y/n)    ").lower()
        if "y" in answer:
            break
        else:
            print("No problem, lets enter it again")
            continue

    # db query
    # make sure the record exists
    cursor.execute('''SELECT id,author,title,quantity FROM books WHERE id == ?''', (_id,))
    # print results of the search
    resultList = cursor.fetchall()
    if len(resultList) == 0:
        print("No books could be located with that ID")
        return 
    try:
        cursor.execute('''UPDATE books SET id = ?, title = ?, author = ?, quantity = ? WHERE id = ? ''',(_id, _title, _author, _quantity, _id))
    except:
        "No entries could be found with that id.Please review the data."

    print("Book updated!")
    print("---------------------------------")


def delete_book():
    #   ○ Delete books from the database                -> Code method
    # delete book by id
    id_to_Delete = input_validator("int", "for the Book´s id to delete")
    # Delete query
    try:
        cursor.execute(
            '''DELETE from books WHERE id = ?''', (id_to_Delete,))
    except:
        "No entries were found in the database with that ID"
    # delete book by author
    # delete book by title

    print("Book deleted!")
    print("---------------------------------")


def search():
    #   ○ Search the database to find a specific book   -> Code method
    # search by id
    id_to_Search = input_validator("int", "for the Book´s id to search")
    # search by author
    # search by title
    # make query
    # cursor.execute('''SELECT id,author,title,quantity FROM books WHERE id = ?''', ((int)(id_to_Search),))
    cursor.execute('''SELECT id,author,title,quantity FROM books WHERE id == ?''', (id_to_Search,))
    # print results of the search
    resultList = cursor.fetchall()
    if len(resultList) == 0:
        print("No books could be located with that ID")
        return
    print("The following books match with your id:")
    print("(id, author, title, quantity)")
    for i in resultList:
        print(i)
    print("---------------------------------")

def debug_print_all():
    # Print all contents of DB:
    cursor.execute('''SELECT id,title, author,quantity FROM books''')
    print("Contents of the Database:")
    for row in cursor:
        print(row)
    print("---------------------------------")
    


# PROGRAM STARTS ------------------------------------------------------------
# - Create database
db = sqlite3.connect('bookstore_contents_DB')
# Create cursor
cursor = db.cursor()

# Create table only if it does not exist
cursor.execute(
    '''SELECT name FROM sqlite_master WHERE type='table' AND name="books"''')
if len(cursor.fetchall()) != 0:
    # This means the table exists. We must drop it, and start anew.
    cursor.execute('''DROP TABLE books''')

cursor.execute('''
CREATE TABLE books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    quantity INTEGER)''')

# Insert the following new rows into the python_programming table
# Create tuples to insert in one go
initial_books = [
    (3001, "A tale of two cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R. Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carrol", 12)]

# Insert rows above
cursor.executemany('''INSERT INTO books(id, title, author, quantity)
VALUES(?, ?, ?, ?)''', initial_books)

# MENU STARTS ---------------------------------------------------------------

print('''Welcome to the Bookstore database software!''')

menu = {
    "a": "Add new books to the database",
    "u": "Update book information",
    "d": "Delete books from the database",
    "s": "Search the database to find a specific book",
    "e": "Exit the program",
    "pp": "Print all contents of DB"
}

while(True):
    # Choose menu option
    menu_option = user_options_input(menu)
    #   ○ Add new books to the database                 -> Code method
    if(menu_option == "a"):
        add_new_book()
    #   ○ Update book information                       -> Code method
    if(menu_option == "u"):
        update_book()
    #   ○ Delete books from the database                -> Code method
    if(menu_option == "d"):
        delete_book()
    #   ○ Search the database to find a specific book   -> Code method
    if(menu_option == "s"):
        search()
    if (menu_option == "pp"):
        debug_print_all()
    #   ○ Exit
    if(menu_option == "e"):
        print("Happy reading!")
        break
