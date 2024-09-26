# %%
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x)**2 + (self.y)**2)**0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

    def halfway(self, p2):
        mx = self.x + (p2.x - self.x)/2
        my = self.y + (p2.y - self.y)/2
        return Point(mx, my)


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, position, w, h):
        """ Initialize rectangle at position, with width w, height h """
        self.corner = position
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    # Part 2 implement grow method here.

    # Part 3 implement move method here.


# %%
box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
print(f"box: {box}")
print(f"bomb: {bomb}")

# %%
box.width += 50
box.height += 100
print(f"box: {box}")

# %%
# Demo Part 2
r = Rectangle(Point(10, 5), 100, 50)
print(r)
r.grow(25, -10)
print(r)

# %%
# Demo Part 3
print(r)
r.move(-10, 10)
print(r)

# %%
