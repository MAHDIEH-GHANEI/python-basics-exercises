#“Find the minimum element in a list without using the built-in min() function.”

num = [50, 14, 65, 8, 15, 17, 2, 69, 70]
a = num[0]

for i in num:
    if a > i :
        a = i
print("The smallest number in the list: ", a)