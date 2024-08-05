import turtle


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """

    # Start of onditional height check
    if height >= 200:
        t.fillcolor("red")
    elif height > 100:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    # End of conditional height check

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(f"  {str(height)}")
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

    # Start of hiding line between bars
    t.penup()
    t.forward(10)
    t.pendown()
    # End of hiding line between bars


wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

# Move tess to the left so that everything is centered.
tess.penup()
tess.left(180)
tess.forward(7 * 50 / 2)
tess.left(180)
tess.pendown()

xs = [48, 117, 200, 240, 160, 260, 220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
