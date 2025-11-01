"""These programs introduce the match-case statement, which works like a switch-case in other languages.
It helps make your code cleaner when handling multiple conditions."""
"""
# (1)  Use of match-case to display weekday names based on number
day_num = int(input("Enter a number (1-7): "))

match day_num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")

"""

# Program 2: Simple Calculator using match-case
# Perform operation based on user choice

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1–4 or symbol): ")

match choice:
    case "1" | "+":
        print("Result =", num1 + num2)
    case "2" | "-":
        print("Result =", num1 - num2)
    case "3" | "*":
        print("Result =", num1 * num2)
    case "4" | "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error: Division by zero!")
    case _:
        print("Invalid choice! Please select a valid operation.")