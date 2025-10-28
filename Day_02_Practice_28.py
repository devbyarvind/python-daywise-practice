# (1) Addition of Three Numbers
# Take three numbers as input from the user, add them, and print the result.

number_one = int(input('Enter Your First Number: '))
number_two = int(input('Enter Your Second Number: '))
number_three = int(input('Enter Your Third Number: '))

Fourth= number_one + number_two + number_three

print(f"The Addition of the Three number is {Fourth} ")

# (2) Convert Float to Integer
# Take a floating number from the user and convert it to integer, then print both values.

first_num = float(input("Enter a Number: "))
print(f"Before Conversion The Value is {first_num}")

second_num = int(first_num)
print(f"The Converted value is {second_num}")

# (3) Swap Two Variables (Without 3rd Variable)
# Take two values from user and swap them without using third variable.

a = eval(input("Enter a First Value: "))
b = eval(input("Enter a Second Value: "))

b,a = a,b

print(f"The Swapping value result is: {a,b}")

# (4) Percentage Calculation
# Take marks of 5 subjects, calculate total and percentage.

marks_1= int(input("Enter a Hindi Marks: "))
marks_2= int(input("Enter a English Marks: "))
marks_3= int(input("Enter a Physics Marks: "))
marks_4= int(input("Enter a Chemistry Marks: "))
marks_5= int(input("Enter a Maths Marks: "))

total_per = (marks_1+marks_2+marks_3+marks_4+marks_5)/5
print(f"The Marks is: {total_per}%")

# (5) Celsius to Fahrenheit
# Take temperature in Celsius and convert to Fahrenheit.

cel = int(input("Enter a Celcious Degree Value: "))

fer = (cel * 9/5) + 32

print(f"The Result of the feranite is {fer}\u00B0F")

# (6) Average of Two Numbers
# Take two numbers from the user and print their average.

average_one = int(input("Enter a First Value: "))
average_two = int(input("Enter a Second Value: "))

total = average_one + average_two
average = total/2
print(f"The Average is: {average} ")

# Average of Two Numbers dynamic Way

count = int(input("How many numbers do you want to enter? "))
total = 0
for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    total += num
average = total / count
print(f"The Average is: {average}")

# (7) Area of Circle
# Take radius from the user and calculate area.

radius_num = float(input("Enter a Radius: "))
area_of_circle = 3.14*radius_num*radius_num
print(f"The Area of Circle is: {area_of_circle}")


# (8) Volume of a Cylinder
#Take radius and height from the user and calculate the volume of the cylinder.

radius = float(input("Enter a Radius of the cylinder:  "))
height = float(input("Enter a Height of the cylinder:  "))

volume = 3.14 * radius**2 * height
print(f"The Volume of the Cylinder Is: {volume}")

# (9) Convert Seconds into Hours, Minutes, and Seconds
# Take total seconds as input and convert it into hours, minutes, and remaining seconds.

second = int(input("Enter a Total Second Value: "))

total_hour= second//3600
total_remaining_second= second % 3600
total_minute = total_remaining_second // 60
total_second = total_remaining_second % 60

print(f"{total_hour} Hour, {total_minute} Minute, {total_second} Second.")

# (10) Convert Days into Years, Weeks, and Days
# Take total days as input and show the equivalent in years, weeks, and days.

total_days_from_user= int(input("Enter a Total Days: "))

total_year = total_days_from_user // 365
# print(total_year)
remaining_days_from_user = total_days_from_user % 365
# print(remaining_days_from_user)
total_week= remaining_days_from_user//7
# print(total_week)
total_day = remaining_days_from_user % 7
# print(total_day)
print(f"{total_year} Year, {total_week} Week, {total_day} Days.")

# (11) Create two variables — one integer and one string — and check how Python treats 0 and empty string ("") in conditional statements.
a = 0 # Zero is considered False
b = "" # Empty string is considered False
if a or b:
    print("True:")
else:
    print("False")


# (12) Take input from the user, store it in a list, and check whether the string "Arvind" exists in that list or not.
# Use the in operator to check membership.

a = [(input("Enter a Value: "))]
print("Arvind" in a)















