#“Write a contact management program that stores names and phone numbers in a list and allows displaying them.”
def contacts(name, number):
    contact = [name, number]
    return contact

name = input("Enter your name: ")
number = int(input("Enter your number: +98 "))

result = contacts(name, number)
print("Contact information: ", result)