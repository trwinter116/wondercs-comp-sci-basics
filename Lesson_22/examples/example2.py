# %%
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

    # Implement __add__, __mul__, and __rmul__ methods.
    def __add__(self, point2):
        return Point(self.x + point2.x, self.y + point2.y)

    def __mul__(self, point2):
        return Point(self.x * point2.x, self.y * point2.y)

    def __rmul__(self, number):
        return Point(self.x * number, self.y * number)

    def reverse(self):
        temp_y = self.y
        self.y = self.x
        self.x = temp_y


# %%
p1 = Point(3, 4)
p2 = Point(5, 7)
str(p1 + p2)

# %%
str(p1 * p2)

# %%
str(2 * p1)

# %%
str(p1 * 2)


# %%
def multadd(x, y, z):
    return x * y + z


# %%
multadd(3, 2, 1)

# %%
p1 = Point(3, 4)
p2 = Point(5, 7)
str(multadd(1, p1, p2))

# %%
str(multadd(p1, p2, 1))


# %%
def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))


# %%
my_list = [1, 2, 3, 4]
front_and_back(my_list)

# %%
# Implement reverse on point to use front_and_back
p = Point(3, 4)
front_and_back(p)

# %%
