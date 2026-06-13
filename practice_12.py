# Write a program that finds the largest number among three given numbers.

number1=int(input("Enter number one: "))
number2=int(input("Enter number twe: "))
number3=int(input("Enter number three: "))

if number1 > number2 and number1 > number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3
print(f"The largest number is: {largest}")

print("The largest number is:", max(number1, number2, number3)) #Second method