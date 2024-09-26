# %%
from test_helper import test


# Write a function which returns the absolute value of a number "x"
# Remember that the absolute value of a number is it's distance from 0
def absolute_value(x):

    # *** Write your code here ***

    return x


test(absolute_value(0) == 0)
test(absolute_value(-5) == 5)
test(absolute_value(9) == 9)
test(absolute_value(-42) == 42)
test(absolute_value(-123) == 123)


# %%
# Write a function that when given the cardinal direction ("N", "E", "S", "W") you are facing
# will return the cardinal direction you would be facing if you turned clockwise one 45 degrees
def turn_clockwise(direction):

    # *** Write your code here ***

    return direction


test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")


# %%
# Write a function that returns the name of the day of the week when passed the number of the day
# of the week. Start with "Sunday" when the number 0 is passed in and "Saturday" for the number 6.
# Fill in the rest.
def day_name(day_number):

    # *** Write your code here ***

    return day_number


test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) is None)


# %%
# Write a function which does the opposite of the above. When given the name of a weekday it returns the
# number of the weekday. "Sunday" would return 0 and "Saturday" would return 6, the rest fall in between.
def day_num(day_name):

    # *** Write your code here ***

    return day_name


test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")


# %%
# Write a function which when given the day of the week (name) and a number of days from that day
# will return the day of the week at which you would arrive. Imagine you leave on a trip on Monday,
# then travel for 4 days, what day of the week would you arrive on? The answer is of course Friday.
def day_add(day, days):

    # *** Write your code here ***

    return day


test(day_add("Monday", 4) == "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")
test(day_add("Sunday", -1) == "Saturday")
test(day_add("Sunday", -7) == "Sunday")
test(day_add("Tuesday", -100) == "Sunday")
