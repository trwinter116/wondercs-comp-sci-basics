import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()  # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()  # Create alex

tess.forward(80)  # Make tess draw equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)  # Complete the triangle

tess.right(180)  # Turn tess around
tess.forward(80)  # Move her away from the origin

for i in [0, 1, 2, 3]:
    alex.forward(50)
    alex.left(90)

wn.mainloop()


# for i in [0,1,2,3]:
#     alex.forward(50)
#     alex.left(90)

# for i in range(4):
#     alex.forward(50)
#     alex.left(90)

# for c in ["yellow", "red", "purple", "blue"]:
#     alex.color(c)
#     alex.forward(50)
#     alex.left(90)

# clrs = ["yellow", "red", "purple", "blue"]
# for c in clrs:
#     alex.color(c)
#     alex.forward(50)
#     alex.left(90)
