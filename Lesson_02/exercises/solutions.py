# %%
# Take the sentence: Let's learn Python! Store each word in a separate variable, then print
# out the sentence on one line using print.

# Example variable assignment: variable = "value"
# Example print expression: print(variable)/print("Some string!")

w1 = "Let's"
w2 = "learn"
w3 = "Python!"
print(w1, w2, w3, sep=" ")

# %%
# Add parenthesis to the below expression to change the value from 4 to -6.

# To execute this file, paste this command into the shell: python exercise2.py
# or copy the expression and paste it into the console.

expression = 6 * (1 - 2)
print(expression)

# %%
# Run this cell. This will give you an error.
# Assign a value to bruce so that bruce + 4 evaluates to 10

bruce = 6
print(bruce + 4)

# %%
# The formula for computing the final amount if one is earning compound interest is given
# on Wikipedia as: P1 = P(1 + (r/n)) ** (n*t)
# P is the original amount of funds
# P1 is th new amount of funds
# r is the nominal annual interest rate
# n is the compounding frequency
# t is the overall length of time the interest is applied (expressed using the same time
#   units as r, usually years)
# Write a Python program that assigns the principal amount of $10000 to variable P, assign
# to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt
# the user for the number of years t that the money will be compounded for.
# Calculate and print the final amount after t years.

# To execute this file, paste this command into the shell: python exercise4.py


def compound_interest(t):
    p = 10000
    n = 12
    r = 0.08
    return p * (1 + (r/n)) ** (n*t)


print(compound_interest(float(input("How many years are you accruing interest for?"))))

# %%
