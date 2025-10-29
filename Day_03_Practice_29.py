
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

# (6) Grade system (90+ = A, 80+ = B, etc.)

student_marks= float(input("Enter a Your Marks Between 0-100: "))

if student_marks >= 90:
    print("Grade A")
elif student_marks >=80:
    print("Grade B")
elif student_marks >=70:
    print("Grade C")
elif student_marks >=60:
    print("Grade D")
else:
    print("You are Fail")

# (7) Find the largest of four numbers
first_num =int(input("Enter You First Number: "))
second_num =int(input("Enter You Second Number: "))
third_num =int(input("Enter You Third Number: "))
fourth_num =int(input("Enter You Fourth Number: "))

if first_num > second_num and first_num>third_num and first_num>fourth_num:
    print(f"The First is Largest Number: {first_num}")
elif second_num>first_num and second_num>third_num and second_num>fourth_num:
    print(f"The Second is Largest Number: {second_num}")
elif third_num>first_num and third_num>second_num and third_num>fourth_num:
    print(f"The Third is Largest Number:  {third_num}")
elif fourth_num>first_num and fourth_num>second_num and fourth_num>third_num:
    print(f"The Fourth is Largest Number:{fourth_num}")
elif first_num==second_num==third_num==fourth_num:
    print("All Are Equal Number")
else:
    print("There are two or more numbers that are equal and largest.")

# (8) Check if a Number is Positive (and within Range 1–100), Zero, or Negative
check_num = int(input("Enter a Number: "))

if check_num >= 1 and check_num <=100:
    print("it is positive")
elif check_num == 0:
    print("The Number is 0 ")

else:
    print("Number is in Minus")




























