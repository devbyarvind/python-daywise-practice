# (1) Print Numbers from 1 to 10
for i in range(1,11):
    print(i)

# (2) Sum of Natural Numbers (1 to N)
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of numbers from 1 to", n, "is:", total)

# (3) Multiplication Table Generator
num_one= int(input("Enter a Table No: "))
for i in range(1,11):
    print(f"{num_one}*{i}={num_one*i}")

# (4) Countdown Using while Loop
n = int(input("Enter a number to start countdown: "))
while n > 0:
    print(n)
    n -= 1
print("Condition Match")

# (5) Skip Multiples of 3
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)
