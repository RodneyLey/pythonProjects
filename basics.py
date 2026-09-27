# Basic Access Control Program

username = input("Enter your username: ")
password = input("Enter your password: ")
age = int(input("Age? "))

password_length = len(password)


# Check the password strength
if password_length < 8:
    password_status = "Too short"
elif 8 <= password_length <= 11:
    password_status = "Eligible"
else:
    password_status = "Strong"


# Check the user's age
if age >= 18:
    age_status = "Passed"
else:
    age_status = "Failed"


# Display the results
print()
print("Username:", username)
print("Password:", password_status)
print("Age verification:", age_status)
print()


# Determine whether access should be granted
if age >= 18 and password_length >= 8:
#if age_status == "Passed" and password_status in ("Eligible", "Strong") :
    print("ACCESS GRANTED")
    print("Welcome", username)
else:
    print("ACCESS DENIED")