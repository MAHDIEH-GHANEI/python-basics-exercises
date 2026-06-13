# Write a program that takes a number as input 
# and determines whether it is even or odd (using the modulo operator `%`).

number =int(input("Enter number: "))
if int(number%2)==0:
    print(number, "your number is even")
else:
    print(number, "your number is odd")