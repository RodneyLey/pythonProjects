#Creating a project that will be used at the bakery to keep track of the time cards for the employees.
#the program will have a function to add employee info
#When the employee clocks in, the program will store the time and date
#When the employee clocks out, the program will store the time and date
#The program will store clock in and clock out times for each employee.
#The program will also calculate the total hours and minutes worked for each employee.
#we will use the datetime module to get the current date and time
#we will use the timedelta module to calculate the difference between two times

#So basically, it will ask the user to enter the employee's name.
#Whether the user wants to clock in or out.
#Then it will store this information in a csv file which is to be calculated every two weeks.
#The user can then get the total hours worked for each employee.


#This is the main function that will be used to run the program
def main():
    #This is the dictionary that will store the employee's name as the key and the value will be a list of dictionaries
    #The dictionaries will store the clock in and clock out time
    #The time will be stored as a string in the format of HH:MM:SS
    employees = {}
    #This is the main loop that will run the program
    while True:
        #This will print the menu options
        print("Menu")
        print("1. Users")
        print("2. Add User")
        #print("3. Clock In")
        #print("3. Clock Out")
        #print("4. Get Total Hours Worked")
        print("3. Exit")
        #This will ask the user to enter their choice
        choice = input("Enter your choice: ")
        #This will check the user's choice
        #If the user enters 1, it will call the add_employee function
        #If the user enters 2, it will call the clock_in function
        #If the user enters 3, it will call the clock_out function
        #If the user enters 4, it will call the get_total_hours_worked function
        #If the user enters 5, it will exit the program
        if choice == "1":
            print("Users")
            sign_in_user(employees)
        elif choice == "2":
            print("Add User")
            add_employee(employees)
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
def sign_in_user(employees):
    #This will ask the user to enter the employee's name
    name = input("Enter the employee's name: ")
    #This will check if the employee is in the dictionary
    #If the employee is in the dictionary, it will ask the user if they want to clock in or out
    #If the employee is not in the dictionary, it will print a message saying the employee is not in the system
    if name in employees:
        print("1. Clock In")
        print("2. Clock Out")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Clock In")
            #clock_in(employees, name)
        elif choice == "2":
            print("Clock Out")
            #clock_out(employees, name)
        else:
            print("Invalid choice")
    else:
        print("Employee is not in the system")

#This function will add an employee to the employees dictionary
def add_employee(employees):
    #This will ask the user to enter the employee's name
    name = input("Enter the employee's name: ")
    #This will check if the employee is already in the dictionary
    #If the employee is already in the dictionary, it will print a message saying the employee is already in the system
    #If the employee is not in the dictionary, it will add the employee to the dictionary
    if name in employees:
        print("Employee is already in the system")
    else:
        employees[name] = []


#This will run the main function when the program is run
if __name__ == "__main__":
    main()
    print()

