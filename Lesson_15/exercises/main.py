# %%
from test_helper import test


class Point:
    """Point class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        """Create a new point at the origin"""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def distance_from_origin(self) -> float:
        return ((self.x) ** 2 + (self.y) ** 2) ** 0.5

    def halfway(self, p2):
        x = (self.x + p2.x) / 2
        y = (self.y + p2.y) / 2
        return Point(x, y)

    # *** WRITE REFLECT_X CODE HERE ***

    # *** WRITE SLOPE_FROM_ORIGIN CODE HERE ***


# Exercise 1
# Write a function which calculates the distance between two points
def distance(p1: Point, p2: Point):

    # *** WRITE YOUR CODE HERE ***

    return


p1 = Point(2, 3)
p2 = Point(6, 6)
test(distance(p1, p2) == 5.0)

# %%

# Exercise 2
# Add a method to the class Point call "reflect_x" which reflects the point across
# the x axis

p = Point(4, 9)
rp = p.reflect_x()
test(rp.y == -9)
test(rp.x == 4)

# %%

# Exercise 3
# Add a method to the class Point call "slope_from_origin" which calculates the slope
# of a line drawn through the point and origin. The m in y=mx+b

p = Point(1, 1)
s = p.slope_from_origin()
test(s == 1)

# %%
