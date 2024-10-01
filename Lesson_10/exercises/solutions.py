import turtle

# Our exercise today is a little bit different. You will be modifying the below script to add
# additional key bindings and handlers. A list of key bindings and handlers is below, but
# make sure to have fun and be creative by coming up with your own once you are comfortable
# with the process!

# Key: 'r', Function: Change Tess' color to red.
# Key: 'g', Function: Change Tess' color to green.
# Key: 'b', Function: Change Tess' color to blue.

# Key: '+', Function: Increase Tess' size, up to a limit of 20.
# Key: '-', Function: Decrease Tess' size, down to a minimum of 1.

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def h4():
    wn.bye()


def h5():
    tess.color("red")


def h6():
    tess.color("green")


def h7():
    tess.color("blue")


def h8():
    current_size = tess.pensize()
    if current_size < 20:
        tess.pensize(current_size + 1)


def h9():
    current_size = tess.pensize()
    if current_size > 1:
        tess.pensize(current_size - 1)


wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")

wn.onkey(h8, "+")
wn.onkey(h9, "-")

wn.listen()
wn.mainloop()