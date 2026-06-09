# Write a program that takes a list of numbers and calculates the average, the largest number, and the smallest number.
# Then store this list in a dictionary (key: name, value: list of numbers).


number_input=input("Enter numbers with space: ")
number=[float(i) for i in number_input.split()]

len_number=len(number)
if len_number==0:
    print("empty list")
else:
    sum_number=sum(number)
    average=sum_number/len_number
    print("Average is: ", average)

    max_number=max(number)
    print("Maximum is: ", max_number)

    min_number=min(number)
    print("Minimum is: ", min_number)

my_dictonary = {
    "number": number
}
print("Dictionary: ", my_dictonary)