#“Write a program that takes a list of numbers, filters out the numbers greater than 10, and prints them.”

number_list = input("Enter numbers with space: ")
number = [int (i) for i in number_list.split()]

greater_than_10 = [] #list for number bigest 10 
###greater_than_10 = [i for i in number if i > 10]

for i in number:
    if i > 10:
        greater_than_10.append(i)
print("Number greater than 10: ", greater_than_10)
