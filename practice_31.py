#“Write a function to calculate the factorial of a number.”

def factoriel(a):
    num = 1
    for i in range(1, a+1):
        num *= i
    return num

result =factoriel(int(input("Enter your number: ")))
print("Factorial of the entered number: ", result)