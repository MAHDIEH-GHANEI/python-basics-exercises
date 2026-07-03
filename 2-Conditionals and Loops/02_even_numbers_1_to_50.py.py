# Print only the even numbers between 1 and 50.

# Method 1: Using conditional statement (if)
print("Method 1:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

print("\n" + "-"*20)  # Just a separator line

# Method 2: Using the step argument in range() (More Efficient)
print("Method 2 (Efficient):")
for i in range(2, 51, 2):
    print(i, end=" ")
