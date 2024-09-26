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


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, position, w, h):
        """ Initialize rectangle at position, with width w, height h """
        self.corner = position
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    # *** WRITE YOUR AREA CODE HERE ***

    # *** WRITE YOUR PERIMETER CODE HERE ***

    # *** WRITE YOUR FLIP CODE HERE ***


# %%

# Exercise 1
# Add a method to the class Rectangle called "area" which calculates the area of
# the rectangle. Area = Width * Height

r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)

# %%

# Exercise 2
# Add a method to the class Rectangle called "perimeter" which calculates the perimeter
# of the rectangle. Perimeter = 2 * Width + 2 * Height

r = Rectangle(Point(0, 0), 10, 5)
test(r.perimeter() == 30)

# %%

# Exercise 3
# Add a method to the class Rectangle called "flip" which swaps the width and height
# of the rectangle.

r = Rectangle(Point(100, 50), 10, 5)
test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)
