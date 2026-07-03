# Contact management program that stores multiple contacts
# and allows displaying them

contacts = []

def add_contact(name, number):
    contacts.append([name, number])


for i in range(3):
    name = input("Enter name: ")
    number = input("Enter phone number: +98 ")
    add_contact(name, number)


print("\nContact list:")
for contact in contacts:
    print("Name:", contact[0], "| Number:", contact[1])