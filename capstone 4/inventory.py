
# ========The beginning of the class==========
class Shoe:
    '''
    In this function, you must initialise the following attributes:
        ● country
        ● code
        ● product
        ● cost
        ● quantity
    '''

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''Add the code to return the cost of the shoe in this method.'''
        return self.cost

    def get_value(self):
        '''Returns the value as per the formula given'''
        return self.quantity * self.cost

    def get_quantity(self):
        '''Add the code to return the quantity of the shoes.'''
        return self.quantity

    def __str__(self):
        '''Add a code to returns a string representation of a class.'''
        return f'''
product:\t{self.product}
code:\t\t{self.code}
country:\t{self.country}
cost:\t\t${self.cost}
quantity:\t{self.quantity}'''

    def __lt__(self, other):
        # cheeky method from  https://stackoverflow.com/questions/3621826/python-minimum-of-a-list-of-instance-variables
        return self.quantity < other.quantity
        # now min(iList) just works


# =============Shoe list===========
# The list will be used to store a list of objects of shoes.
shoe_list = []

# ==========Functions outside the class==============

def inv_not_emtpy():
    if len(shoe_list)==0:
        print("No shoes loaded!")
        return False
    else:
        return True

def validate_input(type, message):
    while True:
        user_input = input((message + "\n"))
        try:
            if type == "type_integer":
                return int(user_input)
            elif type == "type_float":
                return float(user_input)
        except:
            print("The input you chose is not valid. please try again.")


def read_shoes_data():
    '''
    This Will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    with open("inventory.txt", "r") as f:
        for i, line in enumerate(f):
            # skip first line
            if i == 0:
                continue
            # if not first line create object
            else:
                try:
                    # try to create the shoe object out of line
                    words = line.strip("\n").split(",")
                    # append Shoe instance to shoe_list
                    shoe_list.append(
                        Shoe(words[0], words[1], words[2], float(words[3]), int(words[4])))
                    pass
                except:
                    # if we fail, print line where we have the problem
                    print(
                        f"INPUT ERROR!\nLine {i+1} could not be processed. please review the input inventory file.")
                    continue


def capture_shoes():
    '''
    Will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Country,Code,Product,Cost,Quantity
    country = input("Please input the country:\n")
    code = input("Please input the product code:\n")
    name = input("Please input the product name:\n")
    cost = validate_input("type_float","Please input the product cost:")
    quantity = validate_input("type_integer","Please input the product quantity:") 
    shoe_list.append(Shoe(country, code, name, cost, quantity))


def view_all():
    '''
    Will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for shoe in shoe_list:
        print(shoe.__str__())


def re_stock():
    '''
    Will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    lowest_stock_item = min(shoe_list)
    print(f"Item with lowest stock is {lowest_stock_item.product}.\nOnly{lowest_stock_item.quantity} units remaining.")
    items_to_add = validate_input("type_integer","How many items do you want to restock?")
    lowest_stock_item.quantity += items_to_add
    print(f"Ok, added {items_to_add} units to the model.")


def search_shoe():
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''
    code_to_search = input("Please input the product code you wpuld like to search:\n")
    found_shoes = []
    for shoe in shoe_list:
        if shoe.code == code_to_search:
            found_shoes.append(shoe)
    # case no items found:
    if len(found_shoes) == 0:
        print(f"Sorry, found no shoes with code {code_to_search}")
    # if found some:
    else:
        print("We found the following entries with the same code:")
        for shoe in found_shoes:
            print(shoe.__str__())
            print("__________________")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    total_value = 0
    for shoe in shoe_list:
        val = shoe.get_value()
        print(f"{shoe.country}\t\t | {shoe.code}\t\t | {shoe.product}\t\t| ${val} ")
        total_value +=val
    print("________________________________")
    print(f"Total Stock value:    ${round(total_value,2)}")
    print("________________________________")


def highest_qty():
    '''
    Code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    highest_stock_item = max(shoe_list)
    print(f"Highest item in stock is:\n{highest_stock_item.__str__()}.\n\nWe should think about puting it on sale!")



def print_logo():
    print('''
████████████████████████████████████████
██████▓███████████████████████████████▓▓
████▓─██████████████████████████▓▒▒─▒▒▓█
███▓─▓█████████████████████▓▒────▒▓█████
██▓──▓██████████████▓▓▒──────▒▓█████████
█▓────████████▓▒▒────────▒██████████████
█────────────────────▓██████████████████
█───────────────▒▓██████████████████████
█▓──────────▒▓██████████████████████████
███▓▒▒▒▓▓███████████████████████████████
\n''')


# ==========Main Menu=============
print_logo()
print("Welcome to the Nike stocking tool!\nJUST DO IT\n")

while True:
    menu_option = input('''
_______________________________________________________________________
What would you like to do?
"Read shoes data"   - Opens the inventory .txt and loads it into the machine.
"Capture shoes"     - Manually input shoe stock entry and loads it in the machine.
"View all"          - To preview all the inventory items loaded .
"Restock"           - Add units (user input) to the item with the lowest count.  
"Search shoe"       - Prints the inventory item with the code given by user         
"Value per item"    - Prints the value per item of all units in stock  
"Highest quantity"  - Prints the inventory item most in stock. 
"e"                 - Exit the program
_______________________________________________________________________\n''')

    menu_option = menu_option.lower()
    if menu_option == "read shoes data":
        # call reader
        read_shoes_data()
        print(f"Data loaded. Shoe database now has {len(shoe_list)} items")

    elif menu_option == "capture shoes":
        # call capture
        capture_shoes()

    elif menu_option == "view all":
        # call view all
        if inv_not_emtpy():
            view_all()

    elif menu_option == "restock":
        # call re_stock
        if inv_not_emtpy():
            re_stock()

    elif menu_option == "search shoe":
        # call search shoe
        if inv_not_emtpy():
            search_shoe()

    elif menu_option == "value per item":
        # call value per item
        if inv_not_emtpy():
            value_per_item()

    elif menu_option == "highest quantity":
        # call highest quantity
        if inv_not_emtpy():
            highest_qty()

    elif menu_option == "e":
        # exit option
        print("See you soon!\nAnd remember to JUST DO IT")
        print_logo()
        break

    else:
        # any other input
        print("Input not recognised. Please try again.")
