#“Mini Project: Build a simple calculator that takes two numbers and an operator as input.”

def calculator(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    elif op == "*":
        return a * b
    else:
        return "Invalid operator"
    
number_one = int(input("Enter first number: "))
operator = input("Enter operator: ")
number_two = int(input("Enter second number: "))

result = calculator(number_one, operator, number_two)

print("The result is: ",result)