# %%
from test import test


def distance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    return (a**2 + b**2) ** 0.5


test(distance(1, 2, 4, 2) == 3)
test(distance(1, 2, 4, 6) == 5)


# %%
def area(radius):
    # Write a function which calculates area using pi * radius ** 2
    pass


test(area(2) == 12.566)
test(area(4) == 50.264)


# %%
def area2(x1, y1, x2, y2):
    # Write a function which calculates area when given two points using the already
    # written functions above.
    pass


test(area2(1, 2, 4, 2) == 28)
test(area2(1, 2, 4, 6) == 78)

# %%
