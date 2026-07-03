#Use a while loop to repeatedly ask the user for a password until they enter ‘exit’ to break out of the loop.

password = "exit"
user_password = input("Enter a password: ")

while user_password != password:
    print("Try again")
    user_password = input("Enter a password: ")
    
print("Password accepted.")