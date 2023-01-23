#=====importing libraries===========
'''This is the section where you will import libraries'''
import getpass
from datetime import datetime

#====Login Section====

# read user.txt and store users and pass
user_file = open("user.txt",'r')
# store credentials here
credentials = {}
for line in user_file:
    clean_line = line.strip("\n")       # strip line jump at the end
    words = clean_line.split(", ")      # break into user and password
    credentials[words[0]] = words[1]    # hold credentials in dict 

# Start login
while True:
    login = False
    print("Welcome to the task manager program!")
    while True:
        user = input("Please input your user: ")
        # if user recognised:
        if user in credentials:
            while True:
                print("Please enter your password:")
                password = getpass.getpass() #So we do not display it on screen
                if credentials[user] == password:
                    login = True
                    break
                else:
                    print("\tERROR: wrong password. Please try again\n")                        
        # if user not recognised:
        else:
            print("\tERROR: User not in database. Please try again\n")    
        # if login successful, break loop and continue to program 
        if login:
            break
    break
print("\n---------------------------\nLOG IN SUCCESS\n---------------------------\n")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user (admin only)
s - Statistics (Admin only)
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r' and user == "admin":
        print("\n---------------------------\nNEW USER\n---------------------------\n")
        # Request input of a new username
        while True:
            new_user = input("Please input a name for the new user:\t")
            if new_user in credentials:
                print("\tERROR: User name is taken, please choose another one\n")
            else:
                break
        # Request input of a new password
        while True:
            new_pass = input("Please input a password for the account:\t")
            # Request input of password confirmation.
            new_pass_conf = input("Please confirm the password:\t")
            # Check if the new password and confirmed password are the same.
            # If not the same, the user needs to try again
            if new_pass != new_pass_conf:
                print("\tERROR: The passwords do not match. Please try again\n")
            # If they are the same, add them to the user.txt file
            else:
                break

        # add user and pass to the txt file
        with open('user.txt', 'a') as f:
            f.write("\n")
            f.write(new_user + ", " + new_pass) 
        print("\n---------------------------\nSUCCESS: user and password saved!\n---------------------------\n")
        break

    elif menu == 's' and user == "admin":
        # statistics menu only available for admins
        print("\n---------------------------\nSTATS\n---------------------------\n")
        # read and count users.txt
        with open('user.txt', 'r') as f:
            user_count = 0
            for line in f:
                user_count +=1
        # read and count tasks.txt
        with open('tasks.txt', 'r') as f:
            task_count = 0
            for line in f:
                task_count +=1

        print(f"User count:\t\t{user_count}")
        print(f"Task count:\t\t{task_count}")
        print("__________________________________________________________")

        
    elif menu == 'a':
        print("\n---------------------------\nNEW TASK\n---------------------------\n")
        # In this block you will put code that will allow a user to add a new task to task.txt file
        #Prompt a user for the following: 
        #A username of the person whom the task is assigned to
        while True:
            user = input("Please input the user for this task to be assigned:\t")
            if user not in credentials:
                print("\tERROR: User does not exist. Please try again")
            else:
                break
        
        #A title of a task
        task_title = input("Please add a title for the task:\t")

        #A description of the task
        task_description = input("Please add a description for the task:\t")

        #The due date of the task.
        task_date = input("Please add a date for the task(yyyy mm dd):\t")

        #Then get the current date.
        current_date = datetime.today().strftime('%Y %m %d')

        #Add the data to the file task.txt and remember to include the 'No' to indicate if the task is complete.
        with open('tasks.txt', 'a') as f:
            f.write("\n")
            f.write(f"{user}, {task_title}, {task_description}, {current_date}, {task_date}, No") 
        print("\n---------------------------\nSUCCESS: Task added!\n---------------------------\n")
        
    elif menu == 'va':

        print("\n---------------------------\nVIEW ALL TASKS\n---------------------------\n")
        # Read the task from task.txt 
        # Read a line from the file.
        with open('tasks.txt', 'r') as f:
            for line in f:
                print("__________________________________________________________")
                words = line.strip("\n").split(", ")
                print(f'''
Task:\t\t\t{words[1]}
Assigned to:\t\t{words[0]}
Date assigned:\t\t{words[3]}
Due date:\t\t{words[4]}
Task complete?\t\t{words[5]}
Task description:\t{words[2]}
''')
                print("__________________________________________________________")

    elif menu == 'vm':
        # Read the task from task.txt file and print to the console in the format of Output 2 presented in the L1T19 pdf
        print("\n---------------------------\nVIEW MY TASKS\n---------------------------\n")
        # Read a line from the file
        with open('tasks.txt', 'r') as f:
            for line in f:
                print("__________________________________________________________")
                words = line.strip("\n").split(", ")
                if words[0]== user:
                    print(f'''
Task:\t\t\t{words[1]}
Assigned to:\t\t{words[0]}
Date assigned:\t\t{words[3]}
Due date:\t\t{words[4]}
Task complete?\t\t{words[5]}
Task description:\t{words[2]}
''')
                print("__________________________________________________________")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")