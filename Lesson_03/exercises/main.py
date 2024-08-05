# %%
# Write a program which prints "We like Python's turtles!" 1000 times.
# As an added challenge, see how many different ways you can write it and still achieve the same result.

phrase = "We like Python's turtles!"

# *** Write your code here ***

# %%
# Write a program that uses a for loop to print:
# "One of the months of the year is January"
# "One of the months of the year is February"
# ...
# "One of the months of the year is December"

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# *** Write your code here ***

# %%
# Use for loops to make a turtle draw these regular polgons (regular means all
# sides the same length, all angles the same)
# An equilateral triangle
# A square
# A hexagon (six sides)
# An octogon (eight sides)

import turtle

wn = turtle.Screen()
turtle = turtle.Turtle()

# *** Write your code here ***

wn.mainloop()

# %%

# A malfunctioning robot makes a random turn and then takes 100 steps forward, makes another random turn,
# takes another 100 steps, makes another random turn, etc. The robot manufacturer has recorded the angle of
# each turn before the next 100 steps are taken. The data is available as "turns" below. Use a turtle to
# draw the path taken by our malfunctioning robot. (Positive angles are counterclockwise)

import turtle

wn = turtle.Screen()
robot = turtle.Turtle()

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

# *** Write your code here ***

wn.mainloop()
