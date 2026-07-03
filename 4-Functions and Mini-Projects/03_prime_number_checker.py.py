# Write a function that takes an integer as an argument
# and determines whether it is a prime number.

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


try:
    number = int(input("Enter an integer: "))

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

except ValueError:
    print("Please enter a valid integer.")