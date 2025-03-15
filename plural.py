#ask the user to input an acronym
#open a file with acronyms and their meanings
#loop through the file
#check if the acronym is in the dictionary
#return the meaning of the acronym   
# 
# ask the user if they want to add an acronym
# if yes, ask for the acronym and meaning
# add the acronym and meaning to the file
# if no, exit the program  

def getAcronym():
    acronym = input("Enter an acronym: ")
    acronym = acronym.upper()

    found = True
    try: 
        with open("acronyms.txt") as file:
            for line in file:
            #if line.startswith(acronym):
                if acronym in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return
        
    if not found:
        print("Acronym not found")   


def addAcronym():
    acronym = input("Enter an acronym: ")
    meaning = input("Enter the meaning: ")
    with open("acronym.txt", "a") as file:
        file.write(f"{acronym.upper()} - {meaning}\n")

def main():
    while True:
        print("1. Get Acronym")
        print("2. Add Acronym")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            getAcronym()
        elif choice == "2":
            addAcronym()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


main()
