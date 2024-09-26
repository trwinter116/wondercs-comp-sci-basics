from helperFunctions import make_turtle, make_window

wn = make_window("lightgreen", "Dummy Title")
turtle = make_turtle("blue", 1)

# For todays exercises we will all be working off images in the presentation at the same time.
# Write a function for each exercise which can be called in a for loop to create the shape shown.

def draw_square(t, sz):
    for _ in range(4):
        t.forward(sz)
        t.left(90)


def draw_line_of_squares(t, sz, num_squares):
    for _ in range(num_squares):
        draw_square(t, sz)
        t.forward(sz * 2)


def draw_growing_squares(t, sz, distance, num_squares):
    growth = distance * 2
    for _ in range(num_squares):
        draw_square(t, sz)
        t.penup()
        t.right(90)
        t.forward(distance)
        t.right(90)
        t.forward(distance)
        t.right(180)
        t.pendown()
        sz += growth


def draw_regular_polygon(t, sz, n_sides):
    angle = 360 / n_sides
    for _ in range(n_sides):
        t.forward(sz)
        t.left(angle)


def draw_spiral(t, angle=90):
    # Simpler implementation, followed by best practice
    # size = 5
    # for i in range(100):
    #     t.forward(size)
    #     t.left(angle)
    #     size += 1

    for size, _ in enumerate(range(100), start=5):
        t.forward(size)
        t.left(angle)


draw_regular_polygon(turtle, 10, 8)
wn.mainloop()
