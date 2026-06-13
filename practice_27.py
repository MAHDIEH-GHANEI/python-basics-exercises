#“Write a function that takes the radius r of a circle as an argument and calculates its area.”

import math
def circle(r):
    area = (r **2) * math.pi  #area = (r * r) * 3.14
    return area

num = circle(float(input("Enter r: ")))
print("The area of ​​the circle is equal to: ", num)