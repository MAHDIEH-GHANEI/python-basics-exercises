# A program that takes a string (word) and prints its reverse.

string = input("Enter a word : ")

for i in range(len(string)-1, -1, -1):
    print(string[i], end='')
    
print() #create space

#convert list #Second method
stringg = input("Enter a word: ")
lst = list (stringg) #convert to list
lst.reverse() #reverse list
rev = ''.join(lst) #convert string ____ rev = ''.join(list(s)[::-1])
print(rev)