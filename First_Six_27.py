# Write a Python program to take two numbers as input from the user and print their sum.
# (Remember: input() takes value as string. Convert to int before adding.)

a = input("Enter a First Value: ")
b = input("Enter a Second Value: ")
c = int(a) + int(b)
print(c)


# Take input from the user and print the type of the value entered.
# Hint: Use type() function.

"""eval() is powerful but can be dangerous if someone enters malicious Python code.
For learning and classroom use, it is fine ✔
But in real-world applications, it's safer to avoid eval()."""

a = eval(input("Enter your value: "))
print(type(a))

"""Case 2: When Input Could Be Any Type (Better & Safer eval Alternative)
We use literal_eval from ast module:
"""
from ast import literal_eval
a = literal_eval(input("Enter the Value: "))
print(type(a))

# Write a Python program to calculate the area of a rectangle.

width = float(input("Enter a Base: "))
length = float(input("Enter a height: "))
area = 1/2*width*length
print(area)


#Take two values from the user and swap them using a third variable, then print the values before and after swapping.

swap_one = input("Enter a First Value: ")
swap_two = input("Enter a Second Value: ")
print(f"Before Swapping The result is {swap_one,swap_two}")

swap_three = swap_one
swap_one = swap_two
swap_two = swap_three

print(f"After Swapping the Result is {swap_one,swap_two}")

# Simple SI Calculated

principal = float(input("Enter a Principal value : "))
Rate = float(input("Enter a Rate value : "))
time = float(input("Enter a Time value : "))

SI = (principal * Rate * time ) / 100

print(f"The Simple Interest is {SI} Thank You ")

#Take a float number as input and convert it into integer, then print both values.

a = float(input('Enter a Value: '))
print(f"The Result is Before conversion {a}")
c = int(a)
print(f"The Result is After conversion {c}")























