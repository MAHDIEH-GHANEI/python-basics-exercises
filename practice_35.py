#“Remove a duplicate element from a list.”

lst = ["apple", "banana", "mango", "apple"]

#with set
new_list = list(set(lst))
print(new_list)

#with dictionary
new_list_1 = list(dict.fromkeys(lst))
print(new_list_1)

#with for
new_list_2 = []

for i in lst:
    if i not in new_list_2:
        new_list_2.append(i)

print(new_list_2)