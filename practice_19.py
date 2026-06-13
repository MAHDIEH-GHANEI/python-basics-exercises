#Use a while loop to repeatedly ask the user for a password until they enter ‘exit’ to break out of the loop.

password = "exit"
word = input("Enter a password: ")

while word != password:
    print("Try again")
    word = input("Enter a password: ")
    
print("your guess is true")