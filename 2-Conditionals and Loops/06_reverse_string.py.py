# A program that takes a string (word) and prints its reverse.

# first method
string = input("Enter a word : ")

for i in range(len(string)-1, -1, -1):
    print(string[i], end="")
    
print()

# Second method: Convert the string to a list
string2 = input("Enter a word: ")
lst = list(string2)
lst.reverse()
rev = "".join(lst)
print(rev)

# Third method: Using string slicing
word = input("Enter a word: ")
print(word[::-1])