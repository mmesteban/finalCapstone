#=====importing libraries===========
'''This is the section where you will import libraries'''
import getpass
import copy
from datetime import datetime
from os.path import exists

#====GLOBAL VARS=================================================
user_file = "user.txt"
task_file = "tasks.txt"

#====METHODS=====================================================
def read_tasks_file(task_file):
    # reads the tasks file and returns a list of lists of strings
    #    each list represents a line in the tasks file
    #    each string item is an itme from the task

        # Arguments:
    #   task_file: File to write tasks to

    all_user_tasks = []
    with open(task_file, 'r') as f:
        for line in f:
            words = line.strip("\n").split(", ")
            all_user_tasks.append(words)
    return all_user_tasks


def get_users_credentials(user_file):
    # returns credentials in a dict {user:pass}
    # Arguments:
    #   user_file: File to read users + credentials from

    #   read user.txt and store users and pass
    user_file_f = open(user_file,'r')
    # store credentials here
    credentials = {}
    for line in user_file_f:
        clean_line = line.strip("\n")       # strip line jump at the end
        words = clean_line.split(", ")      # break into user and password
        credentials[words[0]] = words[1]    # hold credentials in dict 
    
    user_file_f.close()

    return credentials

def reg_user(user_file):
    # returns credentials in a dict {user:pass}
    # Arguments:
    #   user_file: File to write credentials to
    print("\n---------------------------\nNEW USER\n---------------------------\n")

    # load credentials
    credentials = get_users_credentials(user_file)
    # Declare success state of operation
    success = False
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
    with open(user_file, 'a') as f:
        f.write("\n")
        f.write(new_user + ", " + new_pass) 
    print("\n---------------------------\nSUCCESS: user and password saved!\n---------------------------\n")
    
    # operation success
    success = True
    return success

def add_task(user_file,task_file):
    # Adds task to a file
    # Arguments:
    #   user_file: File to write credentials to
    #   task_file: File to write tasks to

    # Declare success state of operation
    success = False
    print("\n---------------------------\nNEW TASK\n---------------------------\n")
    # load credentials
    credentials = get_users_credentials(user_file)
    # adds a task to the task list
    #get a username of the person whom the task is assigned to
    while True:
        user_to_assign = input("Please input the user for this task to be assigned:\t")
        if user_to_assign not in credentials:
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
    with open(task_file, 'a') as f:
        f.write("\n")
        f.write(f"{user_to_assign}, {task_title}, {task_description}, {current_date}, {task_date}, No") 
    print("\n---------------------------\nSUCCESS: Task added!\n---------------------------\n")
    success = True
    return success

def view_all(task_file):
    # displays all tasks in a task file
    # Arguments:
    #    task_file: file to read the task from

    success = False
    print("\n---------------------------\nVIEW ALL TASKS\n---------------------------\n")
    # Read the task from task.txt 
    # Read a line from the file.
    with open(task_file, 'r') as f:
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
    success = True
    return success

def view_mine(task_file,user, user_file):
    # displays only the current user´s task
    # Arguments:
    #   task_file: file to read the tasks from
    #   user: user to display tasks for
        # call vm method here
            # Read the task from task.txt file and print to the console in the format of Output 2 presented in the L1T19 pdf
    print("\n---------------------------\nVIEW MY TASKS\n---------------------------\n")
    # Read a line from the file
    assigned_user_tasks = []
    all_user_tasks = []
    with open(task_file, 'r') as f:
        for line in f:
            words = line.strip("\n").split(", ")
            all_user_tasks.append(words)
            if words[0]== user:
                assigned_user_tasks.append(words)
                print(f"________________________TASK #{len(assigned_user_tasks)}___________________________")
                print(f'''
Task:\t\t\t{words[1]}
Assigned to:\t\t{words[0]}
Date assigned:\t\t{words[3]}
Due date:\t\t{words[4]}
Task complete?\t\t{words[5]}
Task description:\t{words[2]}
''')
            print("__________________________________________________________")
    # If not tasks assigned for user then return to main menu (exit method)
    if len(assigned_user_tasks) == 0:
        print("No tasks assigned to your user yet. Add one from the menu!")
        sucess = True
        return sucess

    print("____________________END OF ASSIGNED TASKS_________________\n")  
    
    credentials = get_users_credentials(user_file)

    print("____________________PLEASE SELECT A TASK__________________\n")
    
    while True:
        chosen_task_index = int(input("Select one of the previous tasks by its index to edit or mark as complete.\nInput '-1' to return t o the menu\n"))
        # return to menu
        if chosen_task_index == -1:
            sucess = True
            return sucess
        # Let user modify task or mark as complete: bad task index 
        elif chosen_task_index > len(assigned_user_tasks):
            # validate selection: index might not exist
            print("The task number you inputed is not correct. Please select another one")
            # if it does not exist then continue while loop
            continue
        # If it exists: Let user modify task or mark as complete
        else:
            chosen_task = assigned_user_tasks[chosen_task_index-1]
            chosen_task_modified = copy.deepcopy(chosen_task)
            modified = False
            mark_done = input(f"You have selected task {chosen_task_index}. Do you want to mark it as done? (type 'y'/'n')\t").lower()
            if 'y' == mark_done:
                # check if it is done already. If it is, display result.
                if chosen_task[5].lower() == "yes":
                    print("The task you selected is already marked as done. Please select another one")
                    continue
                # If task not done make change.
                else:
                    chosen_task_modified[5] = "Yes"
                    modified = True
            elif 'n' == mark_done:
                print("Ok, no changes saved.")
            else:
                print("You did not input 'y' or'n, so the task was not changed.")
            
            # Ask if user wants to modify the task data IF TASK NOT DONE:
            if chosen_task_modified[5] == "No":
                # Modify asignee?_______________________________________________
                modify_asignee = input("Do you want to change the Asignee? (type 'y'/'n')\t").lower()
                if modify_asignee == 'y':
                    while True:
                        new_asignee = input("Please input the name of the new asignee for the task:\t")
                        if new_asignee in credentials:
                            chosen_task_modified[0] = new_asignee
                            modified = True
                            print(f"OK, asignee modified. New asignee is {new_asignee}")
                            break
                        else:
                            print("The asignee you selected is not recognised in the user database. please try again.")
                elif modify_asignee != 'n':
                    print("You did not input 'y' or'n, so the task asignee was not changed.")
                # Modify due date?_______________________________________________
                modify_date = input("Do you want to change the due date? (type 'y'/'n')\t").lower()
                if modify_date == 'y':
                    new_date = input("Please input the new date due for the task((yyyy mm dd)):\t")
                    chosen_task_modified[4] = new_date
                    modified = True
                    print(f"OK, date modified. New date is {new_date}")
                elif modify_date != 'n':
                    print("You did not input 'y' or'n, so the task due date was not changed.")
            
            #rewrite the task with the new data in tasks.txt IF MODIFIED
            if modified:
                # we can work on the assigned_user_tasks
                for i,task_word_list in enumerate(all_user_tasks):
                    # identify line to rewrite: with chosen_task (same values)
                    same_line = True
                    for j,word in enumerate(task_word_list):
                        if word !=  chosen_task[j]:
                            same_line = False
                            break
                    # replace line with chosen_task_modified    
                    if same_line:
                        all_user_tasks[i] = chosen_task_modified
                        break
                # rewrite the tasks.txt with the new tasks:
                print(all_user_tasks)
                with open(task_file, 'w') as f:
                        for i,t in enumerate(all_user_tasks):
                            s = (f"{t[0]}, {t[1]}, {t[2]}, {t[3]}, {t[4]}, {t[5]}\n")
                            # delete line jump if last task in doc
                            if i == len(all_user_tasks) - 1:
                                s = s[:-1]
                            f.write(s)
                
        sucess = True
            
        input_continue = input("Changes saved. Do you want to  continue making changes? (type 'y' if so)\t").lower()
        # make another change, another while loop run
        if input_continue == 'y':
            continue
        # break while loop and return to exit method
        else:
            break

    sucess = True
    return sucess

def overdue(date):
    # returns true if date introduced is overdue
    # strign date introduced must be in format 'yyyy mm dd'
    introduced_date = date.split()
    print (introduced_date)
    current_date = datetime.today().strftime('%Y %m %d')
    # compare year
    if int(current_date[0]) < int(introduced_date[0]):
        return True
    # compare month
    elif int(current_date[1]) < int(introduced_date[1]):
        return True
    # compare day
    elif int(current_date[2]) < int(introduced_date[2]):
        return True
    else:
        return False

def generate_reports(task_file, user_file):
    # read task file
    all_user_tasks = read_tasks_file(task_file)
    
    complete_task_count = 0
    incomplete_task_count = 0
    overdue_task_count = 0
    task_counter = {}

    credentials = get_users_credentials(user_file)
    for user in credentials:
        task_counter[user + "_task"] = 0
        task_counter[user + "_task_done"] = 0
        task_counter[user + "_task_undone"] = 0
        task_counter[user + "_task_undone_overdue"] = 0

    for task in all_user_tasks:
        # identify user and add task
        task_counter[task[0] + "_task"]+=1

        if 'Yes' in task[5]:
            complete_task_count +=1
            task_counter[task[0] + "_task_done"] += 1
        elif 'No' in task[5]:
            incomplete_task_count +=1
            task_counter[task[0] + "_task_undone"] += 1
        if (overdue(task[4])) and ('No' in task[5]):
            overdue_task_count+=1
            task_counter[task[0] + "_task_undone_overdue"] += 1

    # generate "task_overview.txt"________________________________________________________________
    doc_1 = []
    #    The total number of tasks that have been generated and tracked using the task_manager.py.
    doc_1.append(f"Number of tasks generated and tracked: {len(all_user_tasks)}\n")
    #    The total number of completed tasks.
    doc_1.append(f"Tasks completed:                       {complete_task_count}\n")
    #    The total number of uncompleted tasks.
    doc_1.append(f"Tasks not completed:                   {incomplete_task_count}\n")
    #    The total number of tasks that haven’t been completed and that are overdue.
    doc_1.append(f"Tasks not completed and overdue:       {overdue_task_count}\n")
    #    The percentage of tasks that are incomplete.
    doc_1.append(f"% of tasks not completed:              {round(100 * incomplete_task_count/len(all_user_tasks) , 2)}%\n")
    #    The percentage of tasks that are overdue.
    doc_1.append(f"% of tasks overdue:                    {round(100 * overdue_task_count/len(all_user_tasks) , 2)}%")

    with open("task_overview.txt","w") as w:
        w.writelines(doc_1)
    print("Reports file generated in 'task_overview.txt'!")

    # generate "user_overview.txt"________________________________________________________________
    doc_2 = []
    #    The total number of users registered with task_manager.py.
    doc_2.append(f"The number of users registered is {len(get_users_credentials(user_file))}\n")
    #    The total number of tasks that have been generated and tracked using task_manager.py.
    doc_2.append(doc_1[0])
    doc_2.append("___________________________________________________________________________\n")
    #    For each user: hold task count in a dict 
    for user in credentials:
        doc_2.append(f"___________User '{user}':___________\n")
    #       The total number of tasks assigned to that user.
        key = user + "_task"
        doc_2.append(f"User {user} has been assigned {task_counter[key]} tasks\n")
        if task_counter[key]!=0:
        #       The percentage of the total number of tasks that have been assigned to that user
            doc_2.append(f"User {user} has been assigned {round(100 * task_counter[key]/len(all_user_tasks),2)}% of all tasks.\n")
        #       The percentage of the tasks assigned to that user that have been completed
            percent_done = round(100 * task_counter[user + "_task_done"]/task_counter[key],2)
            doc_2.append(f"User {user} has completed {percent_done}% of his assigned tasks.\n")
        #       The percentage of the tasks assigned to that user that must still be completed
            percent_undone = round(100 * task_counter[user + "_task_undone"]/task_counter[key],2)
            doc_2.append(f"User {user} must still complete {percent_undone}% of his assigned tasks.\n")
        #       The percentage of the tasks assigned to that user that have not yet been completed and are overdue
            percent_undone_overdue = round(100 * task_counter[user + "_task_undone_overdue"]/task_counter[key],2)
            doc_2.append(f"User {user} has  {percent_undone_overdue}% of his assigned tasks overdue.\n")

    with open("user_overview.txt","w") as w:
        w.writelines(doc_2)
    print("Reports file generated in 'user_overview.txt'!")
    

    sucess = True
    return sucess

def view_statistics(task_file, user_file):
    task_overview_file = "task_overview.txt"
    user_overview_file = "user_overview.txt"
    if (not exists(task_overview_file)) and (not exists(user_overview_file)):
        generate_reports(task_file, user_file)
    # read reports and display them on screen
    print("_______________Task report:_______________")
    with open(task_overview_file,'r') as r:
        for line in r:
            print (line)
    print("_______________User report:_______________")
    with open(user_overview_file,'r') as r:
        for line in r:
            print (line)
    
    return True   



def view_statistics_old(task_file,user_file):
    print("\n---------------------------\nSTATS\n---------------------------\n")
    # read and count users.txt
    with open(user_file, 'r') as f:
        user_count = 0
        for line in f:
            user_count +=1
    # read and count tasks.txt
    with open(task_file, 'r') as f:
        task_count = 0
        for line in f:
            task_count +=1

    print(f"User count:\t\t{user_count}")
    print(f"Task count:\t\t{task_count}")
    print("__________________________________________________________")
    sucess = True
    return sucess


#====PROGRAM==========================================================

# load credentials
credentials = get_users_credentials(user_file)
# Start login
login = False
print('''
------------------------------------
Welcome to the task manager program!
------------------------------------
LOGIN
------------------------------------''')
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
print("\n---------------------------\nLOG IN SUCCESS\n---------------------------\n")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if user == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user (admin only)
s - Display Statistics (Admin only)
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports
e - Exit
: ''').lower()

    else:
        menu = input('''Select one of the following Options below:
a - Add a task
vm - View my tasks
e - Exit
: ''').lower()

    if menu == 'r' and user == "admin":
        # call REG method here
        if reg_user(user_file):
            continue
        else:
            break

    elif menu == 's' and user == "admin":
        # statistics menu only available for admins
        if view_statistics(task_file , user_file):
            continue
        
    elif menu == 'a':
        # call add task method
        if add_task(user_file,task_file):
            continue
        else:
            break
    
    elif menu == 'va'and user == "admin":
        if view_all(task_file):
            continue
        else:
            break
    
    elif menu == 'vm':
        if view_mine(task_file,user,user_file):
            continue
        else:
            break
    
    elif menu == 'gr':
        if(generate_reports(task_file,user_file)):
            continue
        else:
            break

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")