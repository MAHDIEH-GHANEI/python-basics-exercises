# A program that takes a number and prints the multiplication table of that number up to 10

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")