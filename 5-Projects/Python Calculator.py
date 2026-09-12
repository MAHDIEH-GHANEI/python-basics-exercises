import math
history = []

def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Please enter a valid number!")

def get_operator(message):
    while True:
        operator = input(message)
        operator = operator.lower()

        if operator in ('+', '-', '*', '/', '//', '%', '**', 'radical', 'sin', 'cos', 'cot', 'tan', 'factorial'):
            return operator
        elif operator == 'exit':
            return 'exit'
        else:
            print("Please enter a valid operator.")

def calculate(operator, number1, number2):
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        result = number1 / number2
    elif operator == '//':
        result = int(number1 / number2)
    elif operator == '%':
        result = number1 % number2
    elif operator == '**':
        result = number1 ** number2
    return result

def calculate_single(operator, number, angle_mode):
    if operator == 'radical':
        while number < 0:
            number = get_number("Please enter a non-negative number: ")

        result = math.sqrt(number)

    elif operator == "sin":
        if angle_mode == "d":
            result = math.sin(math.radians(number))

        elif angle_mode == "r":
            result = math.sin(number)

    elif operator == "cos":
        if angle_mode == "d":
            result = math.cos(math.radians(number))

        elif angle_mode == "r":
            result = math.cos(number) 

    elif operator == "cot":
        if angle_mode == "d":
            tan = math.tan(math.radians(number))

            while tan == 0:
                number = get_number()
                tan = math.tan(math.radians(number))

        elif angle_mode == "r":
            tan = math.tan(number)
            
            while round(tan, 4) == 0:
                number = get_number()
                tan = math.tan(number)

        result = 1 / tan

    elif operator == "tan":
        if angle_mode == "d":
            cos = math.cos(math.radians(number))

            while round(cos, 4) == 0:
                number = get_number()
                cos = math.cos(math.radians(number))


            result = math.tan(math.radians(number))

        elif angle_mode == "r":
            cos = math.cos(number)
            
            while round(cos, 4) == 0:
                number = get_number()
                cos = math.cos(number)


            result = math.tan(number) 

    elif operator == 'factorial':
        while number < 0 or number % 1 != 0:
            number = get_number("Please enter a non-negative integer: ")
        result = math.factorial(int(number))
    return result

def get_angle_mode():
    angle_mode = input("degree or radian?(d/r): ")
    angle_mode = angle_mode.lower()

    while angle_mode not in ('d', 'r'):
        print("Please just enter 'd' or 'r': ")
        angle_mode = input("degree or radian?(d/r): ")
        angle_mode = angle_mode.lower()
    
    return angle_mode

print("========================\n"
        "       CALCULATOR\n"
        "========================")           
number1 = get_number("Please enter first number: ")
operator = get_operator("Enter operator (+, -, *, /, //, %, **, 'radical', 'sin', 'cos', 'cot', 'tan', 'factorial'): ")
if operator != 'exit':
    angle_mode = None
    if operator in ('radical', 'sin', 'cos', 'cot', 'tan', 'factorial'):

        if operator in ('sin', 'cos', 'tan', 'cot'):
            angle_mode = get_angle_mode()

        result = calculate_single(operator, number1, angle_mode)
        history.append((number1, operator, None, result))

        print("Result: ", result)

    else:
        number2 = get_number("Please enter second number: ")

        if operator in ('/', '//', '%'):
            while number2 == 0:
                number2 = get_number("Please enter second number: ")

        result = calculate(operator, number1, number2)
        history.append((number1, operator, number2, result))
        print("Result", result)

    while True:

        operator = get_operator("Please enter operator: ")

        if operator == 'exit':
            print("Result", result)
            print("Goodbye, take care")
            break

        elif operator in ('radical', 'sin', 'cos', 'cot', 'tan', 'factorial'):

            angle_mode = None

            if operator in ('sin', 'cos', 'tan', 'cot'):
                angle_mode = get_angle_mode()
            
            old_result = result
            result = calculate_single(operator, result, angle_mode)

            print("Result: ", result)

            history.append((old_result, operator, None, result))

        else:
            number3 = get_number("Please enter next number: ")

            if operator in ('/', '//', '%'):
                while number3 == 0:
                    number3 = get_number("Please Enter a number other than zero: ")

            old_result = result
            result = calculate(operator, result, number3)
            history.append((old_result, operator, number3, result))
            print("Result", result)

print("========================")
print("        HISTORY")
print("========================")

for number1, operator, number2, result in history:
    if number2 is None:
        print(number1, operator, "=", result)
    else:
        print(number1, operator, number2, "=", result)
print("\n========================")