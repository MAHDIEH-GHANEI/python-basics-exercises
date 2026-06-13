# Number guessing game (the program has a number in mind and the user guesses it).
import random as rn
answer = rn.randint(1 , 100)
guess = int(input("Enter your guess: "))

while guess != answer:
    if guess > answer:
        print("Your guess is big")
    else:
        print("Your guess is small")
    guess = int(input("Enter new guess: "))

print("you win!")

#To manage the input type
try:
    guess = int(input("Enter new guess: "))
except ValueError:
    print("Please enter a valid number!")