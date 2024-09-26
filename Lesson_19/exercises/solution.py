# %%

# Exercise 1
# Write a function named readposint that uses the input dialog to prompt the user for a
# positive integer and then checks the input to confirm that it meets the requirements.
# It should be able to handle inputs that cannot be converted to int, as well as negative
# ints, and edge cases (e.g. when the user closes the dialog, or does not enter anything
# at all.)

def readposint():

    user_input = input("Please enter a positive number: ")

    if user_input == '':
        raise ValueError("Please enter a value.")

    try:
        number = int(user_input)
    except ValueError as e:
        raise ValueError("Your input must be a number.") from e

    if number < 0:
        raise ValueError("Your input must be positive, it cannot be negative.")

    return number

readposint()
# %%
