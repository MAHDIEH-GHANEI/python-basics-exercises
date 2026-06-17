#“Write a program that uses the datetime module to display the current date and time,
#  and the random module to generate a random number between 1 and 100.”

import random 
import datetime

number_random = random.randint(1, 100)
print("Random Number: ", number_random)

clock = datetime.datetime.now()
print("Current Date & Time: ", clock)