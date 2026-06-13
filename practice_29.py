#“Write a function that takes a list as an argument and returns only the even numbers from it.”

def list_even(my_list):
    number1 = []

    for i in my_list:
        if i % 2 == 0:
            number1.append(i)
            
    return number1

a = [4, 5, 76, 95, 40, 13, 20]
print(list_even(a))