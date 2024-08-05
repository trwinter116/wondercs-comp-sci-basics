import turtle

# There are two things that need to be updated in this program:
# **** ALL CODE SHOULD BE WRITTEN INSIDE THE DRAW BAR FUNCTION ****
# 1. draw_bar needs to be updated so that a line is not drawn between each bar.
# 2. draw_bar needs to be updated so that the bar color follows the below rules:
#    a. if the height is 200 or more, the bar must be colored red.
#    b. if the height is between 100 and 200, the bar must be colored yellow.
#    c. if the height is 100 or less, the bar must be colored green.


def draw_bar(t, height):
    """Get turtle t to draw one bar, of height."""
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
    t.forward(10)


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
