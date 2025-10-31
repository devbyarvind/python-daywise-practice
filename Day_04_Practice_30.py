# (1) Write a program to check if a number is less than 10 or greater than 50.

number_one = int(input("Enter Your Number: "))

if number_one <10:
    print("Number is Less than 10")
elif number_one >50:
    print("Number is Greater than 50")
else:
    print("Number is not less than 10 or greater than 50 ")



# (2) Write a program to check if a character entered by the user is not a vowel.


a = str(input("Enter a Character: "))

if not a in ['a', 'e', 'i', 'o', 'u']:
    print("its Consonant")
else:
    print("Its vowels")
# (3) Write a program to check if a person’s entered city is not “Delhi” or “Mumbai”, then print “Service not available.”

City= input("Enter a City: ")
if not City in ["Delhi","Mumbai"]:
    print("Service Is Not Available")

else:
    print("Service is Available")

# (4) Write a program to check if a student failed in any subject (marks < 33 in any of 3 subjects).
subject_one = input("Enter a Science Number:")
subject_two = input("Enter a Maths Number:")
subject_three = input("Enter a English Number:")

if subject_one < "33" or subject_two <"33" or subject_three <"33":
    print("You are Fail")
else:
    print("You are Pass")

#(5) Write a program to check if a number is not divisible by 3 or not divisible by 5.
number_1= int(input("Enter a Number: "))

if not number_1 % 3==0 or not number_1 % 5==0:
    print("Its not Divisible by 3 and 5")

else:
    print("its Divisible")

#(6) Write a program to check if a user’s entered password is empty or too short (less than 6 characters).
password = input("Enter a Password: ")

if password == "" or len(password) < 6:
    print("The Password is Empty or You Entered a less than 6 Character")

else:
    print("Password is Correct")


# (7) Write a program to check if an entered day is not Saturday or Sunday, then print “It’s a weekday.”
day_1 = input("Enter a Day Name: ").lower()

if not day_1 in ["saturday","sunday"]:
    print("Its Weekday")

else:
    print("its Holiday")











