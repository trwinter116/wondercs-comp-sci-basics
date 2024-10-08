# %%

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

    # Part 3 implement distance from origin method

    # Part 4 implement __str__ method

    # Part 6 implement midpoint as halfway method


# Part 5 implement midpoint functions


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
# Demo Part 5

p1 = Point(1,1)
p2 = Point(3,3)
print(midpoint(p1, p2))

# %%
# Demo Part 6

p1 = Point(1,1)
p2 = Point(3,3)
print(p1.halfway(p2))

# %%
