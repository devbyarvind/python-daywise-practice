# (1) Compare Two Numbers
# Take two numbers as input from the user and print which one is greater, or if they are equal.

number_one = int(input("Enter a First Number: "))
number_two = int(input("Enter a Second Number: "))

if number_one > number_two:
    print(f"The First number is Greater: {number_one}")
elif number_two > number_one:
    print(f" The Second Number is Greater: {number_two}")
elif number_one == number_two:
    print("Both Numbers are Equal")
else:
    print("Invalid input, please try again.")

# (2) Take age from the user and check if they are eligible to vote.
# (A person can vote if age ≥ 18)

age = int(input("Enter Your Age to check You are Eligible to vote or Not: "))

if age>=18:
    print(f" You are eligible to vote! Your age: {age}")
else:
    print("You are not eligible to vote. Please wait",18-age, "more years")


# (3) Take three numbers as input and find the largest number using logical operators

a = int(input('Enter a First Number: '))
b = int(input('Enter a Second Number: '))
c = int(input('Enter a Third Number: '))

if a>b and a>c:
    print("First is Largest: ",a)
elif b>a and b>c:
    print("Second is Largest: ",b)
elif a==b==c:
    print("All Number is Equal ")
else:
    print("Third is Largest: ",c)

# (4) Ask the user to enter a number and check if it lies between 10 and 50 (inclusive).

user_number = float(input("Enter a Number Between 10 to 50: "))

if user_number >= 10 and user_number <= 50:
    print("The Number lies between 10 to 50 ")
else:
    print("The Number is not between 10 and 50")


# (5) Take a username and password from the user.
# If the username is "admin" and password is "1234", print "Login Successful".
# Otherwise, print "Access Denied".

username= input("Enter Your Username: ")
user_pass= input("Enter You Password: ")

if username =="admin" and user_pass =="12345":
    print("Login Successful")

else:
    print("Access Denied")




































