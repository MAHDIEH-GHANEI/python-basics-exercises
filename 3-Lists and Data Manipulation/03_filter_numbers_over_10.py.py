# Write a program that takes a list of numbers, filters out the numbers
# greater than 10, and prints them.

number_list = input("Enter numbers separated by spaces: ")
numbers = [int(i) for i in number_list.split()]

greater_than_10 = []  # Store numbers greater than 10
# Alternatively:
# greater_than_10 = [i for i in numbers if i > 10]

for i in numbers:
    if i > 10:
        greater_than_10.append(i)

print("Numbers greater than 10:", greater_than_10)