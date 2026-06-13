#“Write a program that takes the names of three friends, adds them to a list, and then sorts the list.”

name = []
for i in range(3):
    a = input("Enter name your friends: ")
    name.append(a)
print("The sorted list of friends is: ", sorted(name))