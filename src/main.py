import re

file_name = input('Enter a file name: ')
file_name = file_name + '.csv'

# Function to read the previous_ID from the file
def read_previous_id():
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip()
            parts = last_line.split(';')
            if len(parts) >= 2 and parts[0].isdigit():
                return int(parts[0])
    return 0  # Default to 0 if no previous ID is found

previous_ID = read_previous_id()

def start_scratch():
    global previous_ID  # Declare previous_ID as a global variable
    # Open the file in read mode ('r')
    with open(file_name, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()

        # Check if there are lines in the file
        if lines:
            # Get the last line
            last_line = lines[-1].strip()  # Get the last line and remove leading/trailing whitespace

            # Split the last line by semicolon
            parts = last_line.split(';')

            # Check if there are enough parts (at least two) and the second part is numeric
            if len(parts) >= 2 and parts[0].isdigit():
                previous_ID = parts[0]  # Save the first part (before semicolon) as the desired value
                
    month = input('Input the month of the year of the transaction (1-12) : ')
    day = input('Input the day of the month of the transaction : ')
    year = input('Input the year of the transaction (YYYY) : ')

    date = (month+'/'+day+'/'+year)
    print(date)

    transaction_name = input('Input the name of the transaction: ')
    transaction_type = input('Type of transaction. Income (0), Expense (1): ')
    transaction_amount = input('Input the amount for the transaction: ')
    group_ID = input('Enter the group ID (1-5):\n1 - School Savings;Money saved for education (20%)\n2 - Savings;Money that is saved for large purchases (15%)\n3 - Free Spend;Money that I can freely spend (40%)\n4 - Tithe;Money to donate (10%)\n5 - Insurance;Money set aside for insurance (15%)\n')
    group_names = ['School Savings;Money saved for education (20%);rgb(192,97,203);','Savings;Money that is saved for large purchases (15%);rgb(53,132,228);','Free Spend;Money that I can freely spend (40%);rgb(246,211,45);','Tithe;Money to donate (10%);rgb(255,120,0);','Insurance;Money set aside for insurance (15%);rgb(237,51,59)']

    group_details = group_names[int(group_ID) - 1]

    with open(file_name, 'a') as file:
        file.write(
            str(int(previous_ID)+1)
            +';'
            +date
            +';'
            +transaction_name
            +';'
            +transaction_type
            +';0;-1;;'
            +transaction_amount
            +';rgb(53,132,228);1;'
            +group_ID
            +';'
            +group_details
            +';'
        )
        
    print("Transaction added successfully.")

# Function to validate the date format

def start_premade():
    global previous_ID  # Declare previous_ID as a global variable
    input_line = input("Enter a line from the official meredian website .csv exported file : ")
    parts = input_line.split(',')
    transaction_name = parts[3]
    raw_date = parts[1]
    date1 = raw_date.split(' ')
    date2 = date1[0]
    date3 = (date2.split('-'))
    date = (date3[0]+'/'+date3[1]+'/'+date3[2])
    transaction_type = input('Type of transaction. Income (0), Expense (1): ')
    transaction_amount = parts[5]
    group_ID = input('Enter the group ID (1-5):\n1 - School Savings;Money saved for education (20%)\n2 - Savings;Money that is saved for large purchases (15%)\n3 - Free Spend;Money that I can freely spend (40%)\n4 - Tithe;Money to donate (10%)\n5 - Insurance;Money set aside for insurance (15%)\n')
    group_names = ['School Savings;Money saved for education (20%);rgb(192,97,203);','Savings;Money that is saved for large purchases (15%);rgb(53,132,228);','Free Spend;Money that I can freely spend (40%);rgb(246,211,45);','Tithe;Money to donate (10%);rgb(255,120,0);','Insurance;Money set aside for insurance (15%);rgb(237,51,59)']

    group_details = group_names[int(group_ID) - 1]
    
    with open(file_name, 'a') as file:
        file.write(
            str(int(previous_ID)+1)
            +';'
            +date
            +';'
            +transaction_name
            +';'
            +transaction_type
            +';0;-1;;'
            +transaction_amount
            +';rgb(53,132,228);1;'
            +group_ID
            +';'
            +group_details
        )

# Choose whether to start from scratch or use a premade input line
choice = input("Choose an option:\n1 - Start from scratch\n2 - Use a premade input line\n")
if choice == "1":
    start_scratch()
elif choice == "2":
    start_premade()
else:
    print("Invalid choice.")

