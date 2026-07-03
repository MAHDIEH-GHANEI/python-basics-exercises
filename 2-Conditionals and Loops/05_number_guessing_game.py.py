# Number guessing game (the program has a number in mind and the user guesses it).

import random as rn

answer = rn.randint(1 , 100)

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue #restart the loop

    if guess == answer:
        print("You win!")
        break
    elif guess > answer:
        print("Your guess is big")
    else:
        print("Your guess is small")