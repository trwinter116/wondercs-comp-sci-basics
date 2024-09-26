# %%
from test_helper import test


def absolute_value(x):
    return -x if x < 0 else x


test(absolute_value(0) == 0)
test(absolute_value(-5) == 5)
test(absolute_value(9) == 9)
test(absolute_value(-42) == 42)
test(absolute_value(-123) == 123)


# %%
def turn_clockwise(direction):
    compass_clockwise = {"N": "E", "E": "S", "S": "W", "W": "N"}
    return compass_clockwise[direction]


test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")


# %%
def day_name(day_number):
    if day_number > 6:
        return
    day_dict = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }
    return day_dict[day_number]


test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) is None)


# %%
def day_num(day_name):
    day_dict = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
    }
    if day_name not in day_dict:
        return
    return day_dict[day_name]


test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")


# %%
def day_add(day, days):
    day_int = day_num(day)
    new_num = day_int + days
    if new_num < 0:
        new_num = new_num + 7

    if new_num < 0:
        new_num = new_num * -1

    if new_num > 6:
        new_num = new_num % 7
    return day_name(new_num)


test(day_add("Monday", 4) == "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")
test(day_add("Sunday", -1) == "Saturday")
test(day_add("Sunday", -7) == "Sunday")
test(day_add("Tuesday", -100) == "Sunday")
