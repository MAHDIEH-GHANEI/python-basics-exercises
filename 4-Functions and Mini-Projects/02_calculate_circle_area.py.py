# Write a function that takes the radius of a circle as an argument
# and calculates its area.

import math

def calculate_circle_area(radius):
    area = radius ** 2 * math.pi
    return area

result = calculate_circle_area(float(input("Enter the radius: ")))

print("The area of the circle is:", result)