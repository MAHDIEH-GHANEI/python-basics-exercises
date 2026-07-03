# Write a function that takes a list as an argument
# and returns only the even numbers from it.

def get_even_numbers(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


numbers_list = [4, 5, 76, 95, 40, 13, 20]

print(get_even_numbers(numbers_list))