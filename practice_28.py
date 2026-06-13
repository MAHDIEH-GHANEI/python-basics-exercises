#“Write a function that takes an integer as an argument and determines whether it is a prime number or not.”

def is_prime(a):
    if a <= 1:
        return False
    
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True
try:
    number = int(input("Enter your number: "))
    
    if is_prime(number):
        print(f"{number} is prime!")
    else:
        print(f"{number} is not prime.")
except ValueError:
    print("Please enter a valid integer!") 