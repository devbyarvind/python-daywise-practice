# (1) How can you remove duplicate numbers from a list and use the Error Handling?
try:
    number = list(map(int, input("Enter a Number: ").split(',')))
    unique_number = list(dict.fromkeys(number))
    print(unique_number)
except ValueError:
    print("Please enter a Valid Number in Sequence like- 1,1,1,1,2,2,2,3,4: ")
finally:
    print("Thank You")

# (2) How can you remove duplicate numbers from a list

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

# (3) Find max & min in a list.

numbers = [10, 45, 2, 99, 23, 56]
max_num = max(numbers)
min_num = min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)

# (4) Reverse a list without using reverse()

numbers = [10, 45, 2, 99, 23, 56]
numbers_one=numbers[::-1]
print(numbers_one)

# (5) Find the second largest element.

number= [10, 45, 2, 99, 23, 56]
largest_one=max(number)

number.remove(largest_one)
second_largest= max(number)
print(second_largest)


# (6) Find common elements between two list.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)


# (7) Find common elements between two String.
list1 = input('Enter a Word: ')
list2 = input('Enter a Word: ')

common_elements = set(list1) & set(list2)
print("Common elements:", common_elements)

















