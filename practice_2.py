#Write a Python program to calculate the Body Mass Index (BMI).

weight =float(input("Please enter your weight: "))
height =float(input("Please enter your height: "))

bmi  =(weight / (height**2))

if bmi < 18.5:
    print("Under weight")
elif bmi < 25:
    print("Normal")
elif bmi < 30 :
    print("Over weight")
elif bmi < 35 :
    print("Obese")
else:
    print("Extremly obese")