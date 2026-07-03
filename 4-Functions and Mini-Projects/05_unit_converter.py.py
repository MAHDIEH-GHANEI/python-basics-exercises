# Write a program to convert units (for example, kilometers to meters).

def kilometers_to_meters(kilometers):
    return kilometers * 1000

result = kilometers_to_meters(float(input("Enter kilometers: ")))

print("Converted value in meters:", result)