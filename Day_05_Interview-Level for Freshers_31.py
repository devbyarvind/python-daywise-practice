
# (1) Employee Eligibility Check
"""
Write a program that asks for an employee’s age and years of experience.
If the person is older than 21 and has at least 2 years of experience, print "Eligible for Job".
Otherwise, print "Not Eligible".
"""
age = int(input("Enter Your Age: "))
year_of_exp = int(input("Enter Your Experience: "))

if age >=21 and year_of_exp >=2:
    print("Eligible For Job")
else:
    print("Not Eligible")

# (2) Discount Eligibility Based on Purchase
"""
If the amount is greater than ₹5000 or the customer is a premium member (Y/N), print "Discount Available".
Else, print "No Discount".
"""
purchase_amount= (input('Enter Your Amount or Are You Premium Customer or Not: '))

if purchase_amount.lower() =="yes":
    print("Discount Available")
else:
    purchase_value= int(purchase_amount)
    if purchase_value >= 5000:
        print("Discount Available")
    else:
        print("Discount Not Available")

# (3) Student Grade Validation
"""
Input marks for three subjects.
If any subject is below 33, print "Fail".
Else if the average is 60 or more, print "First Division".
Else print "Second Division".
"""
sub_1=int(input("Enter You English Subject Marks: "))
sub_2=int(input("Enter You Hindi Subject Marks: "))
sub_3=int(input("Enter You Maths Subject Marks: "))

if sub_1 <33 or sub_2 <33 or sub_3 <33:
    print("You are Fail")
elif (sub_1+sub_2+sub_3)/3 >= 60:
    print("First Division")
else:
    print("Second Division")

# (4) Wi-Fi Connection Check
"""
Ask the user for Wi-Fi status and signal strength (values: "Connected" or "Not Connected", and "Strong", "Weak").
If Wi-Fi is connected and signal strength is strong, print "Stable Internet".
Else print "Unstable Connection".
"""
wifi_status = input("Enter a Wifi Status: ").lower()
wifi_strength = input("Enter a Wifi Strength: ").lower()

if wifi_status=="connected" and wifi_strength=="strong":
    print('Stable Internet')
else:
    print("Unstable Internet")

# (5) Login Validation
"""
Take two inputs — username and password.
If both match "admin" and "1234", print "Login Successful".
Else if username is correct but password is wrong, print "Incorrect Password".
Otherwise, print "Invalid User".
"""
user_1 = input("Enter a Username: ").lower()
pass_1 = int(input("Enter a Password: "))

if user_1 =="admin" and pass_1==12345:
    print("Login Successful")
else:
    print("Invalid User")

# (6) Check if a Number is a Two-Digit Even Number
"""
Ask the user for a number.
If it’s between 10 and 99 (inclusive) and divisible by 2, print "Two-digit Even Number".
Otherwise, print "Not a Two-digit Even Number".
"""
number_1 = int(input("Enter a two digit no:  "))

if number_1 >=10 and number_1 <=99:
    if number_1 %2==0:
        print("Its Two Digit even No")
    else:
        print("Its Two-digit Odd Number")
else:
    print("Number is not a Two Digit")

# (7) Validate Email Input
"""
Ask the user to enter an email address.
If the email is empty or does not contain "@" or ".", print "Invalid Email".
Else print "Email Accepted".
"""
user_email= input("Enter You Email ID: ")
if  user_email == "" or "@" not in user_email or "." not in user_email:
    print("Invalid Email")
else:
    print("Email Accepted")

# (8) Temperature Safety Check
"""
Input current temperature.
If temperature is below 0, print "Freezing Warning".
If it’s between 0 and 35, print "Normal Temperature".
If it’s above 35, print "High Temperature Alert".
"""
temperature = int(input("Enter a Temperature Value: "))

if temperature < 0:
    print("Freezing Warning")
elif temperature >0 and temperature <=35:
    print("Normal Temperature")
else:
    print("High Temperature Alert")

# (9) Mobile Plan Availability
"""
Ask the user for their city and plan type ("Basic", "Premium").
If the city is not in "Delhi", "Mumbai", "Pune" or plan is "Basic", print "Limited Access".
Else print "Full Access".
"""

city= input("Enter Your City Name: ").lower()
plan_type= input("Enter Your Plan Name: ").lower()

if not city in ["delhi","mumbai","pune"] or plan_type =="basic":
    print("Limited Access")
else:
    print("Full Access")

# (10) Secure Password Validation
"""
Take a password as input.
If password is empty, print "Password cannot be empty".
Else if password length is less than 6, print "Password too short".
Else if "@" not in password, print "Add at least one special character".
Else print "Password Accepted".
"""

password_1 = input("Enter your Password to check The Validation: ")

if password_1 == "":
    print("Password cannot be empty")
elif len(password_1) < 6:
    print("Password too short")
elif "@" not in password_1:
    print("Add at least one special character")
else:
    print("Password Accepted")








