#“Write a program to convert units (for example, kilometers to meters).”

def kilometer_to_meter(kilometer):
    return kilometer * 1000

result = kilometer_to_meter(float(input("Enter kilometer: ")))
print("Kilometers to meters Entered number: ", result)