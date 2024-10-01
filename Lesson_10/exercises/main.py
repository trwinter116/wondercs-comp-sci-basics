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


wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.listen()
wn.mainloop()
