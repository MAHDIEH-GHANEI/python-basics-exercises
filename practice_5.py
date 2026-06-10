# Write a program that takes a numerical input from the user.
# If the user does not enter a number, display an appropriate error message and ask again.
# If zero is entered, define and raise a custom error (like ZeroDivisionError or similar).

# Define a custom error for zero
class ZeroInputError(Exception):
    """Custom exception raised when the input is zero."""
    pass

while True:
    try:
        user_input = input("Please enter a number: ")

        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            continue

        number = int(user_input)

        if number == 0:
            raise ZeroInputError("Input cannot be zero.")
        
        print(f"Number entered: {number}")
        break

    except ValueError:
        print("Error: Please enter only numbers.")

    except ZeroInputError as e:
        print(f"Error: {e}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")