# Write a program that takes a number as input 
# and determines whether it is even or odd (using the modulo operator `%`).

number = int(input("Enter a number: "))
if number%2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")