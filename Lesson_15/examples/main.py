# %%

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    # Part 3 implement distance from origin method
    def distance_from_origin(self):
        return ((self.x)**2 + (self.y)**2)**0.5

    # Part 4 implement __str__ method
    def __str__(self):
        return f"({self.x}, {self.y})"
    # Part 6 implement midpoint as halfway method

    def halfway(self, p2):
        mx = self.x + (p2.x - self.x)/2
        my = self.y + (p2.y - self.y)/2
        return Point(mx, my)


# Part 5 implement midpoint functions
def midpoint(p1: Point, p2: Point):
    mx = p1.x + (p2.x - p1.x)/2
    my = p1.y + (p2.y - p1.y)/2
    return Point(mx, my)


# %%
p = Point()
print(p.x)
print(p.y)

# %%
# Demo Part 2
p = Point(x=2, y=3)
print(p.x)
print(p.y)

# %%
# Demo Part 3
p = Point(2, 3)
d = p.distance_from_origin()
print(d)

# %%
# Demo Part 4
p = Point(2, 3)
print(p)

# %%
sp = str(p)
sp
# %%
p1 = Point(1,1)
p2 = Point(3,3)
print(midpoint(p1, p2))
# %%
p1 = Point(1,1)
p2 = Point(3,3)
print(p1.halfway(p2))
# %%
