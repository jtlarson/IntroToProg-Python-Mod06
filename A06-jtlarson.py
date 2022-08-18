# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# jtlarson,8.10.2022, Modified code to complete assignment 06
# jtlarson,8.15.2022, Edited variable names to avoid global shadowing, refined function header descriptions
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            a_task, a_priority = line.split(",")
            row = {"Task": a_task.strip(), "Priority": a_priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task_name, task_priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task_name: (string) with name of task
        :param task_priority: (string) with name of priority
        :param list_of_rows: (list) table list where row will be appended
        :return: (list) of dictionary rows
        """
        row = {"Task": task_name, "Priority": task_priority}
        # Append row dictionary to list of rows (table)
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(row_id, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param row_id: (int) index of row to be deleted
        :param list_of_rows: (list) table list containing row to be deleted
        :return: (list) of dictionary rows
        """
        # Check if the selected index is valid before deleting to avoid errors
        if row_id in range(0, len(list_of_rows)):
            list_of_rows.pop(row_id)
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file
        :param list_of_rows: (list) to write to file
        :return: (list) of dictionary rows
        """
        # Open the file and write each row of data in CSV format
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        return list_of_rows

# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        max_task_chars_int = 0  # the length of the task name
        # Find the longest task name
        for row in list_of_rows:
            if len(row['Task']) > max_task_chars_int:
                max_task_chars_int = len(row['Task'])
        # Display indexed list of records
        row_count_int = 0
        print("ID:", "Task", " " * (max_task_chars_int - 4), "|", "Priority")
        for row in list_of_rows:
            print(row_count_int, ":", row['Task'], " " * (max_task_chars_int - len(row['Task'])), "|", row['Priority'])
            row_count_int += 1

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        task = None
        priority = None
        # If either task or priority is missing, ask again...
        while not task or not priority:
            task = str(input("What task do you want to add?: ").strip())
            priority = str(input("What priority is this task?: ").strip())  # store as a string
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (int) with task
        """
        task_id_int = int(input("Enter the ID to remove: ").strip())
        return task_id_int

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task_str, priority_str = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task_name=task_str, task_priority=priority_str, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing task based on row index
        task_id = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(row_id=task_id, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor .write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
