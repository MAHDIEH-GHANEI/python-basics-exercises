# Write a program that takes the names of three friends, adds them to a list,
# and then sorts the list.

friends = []

for i in range(3):
    friend = input("Enter a friend's name: ")
    friends.append(friend)

print("Sorted list of friends:", sorted(friends))