import turtle


def make_window(color, title):
    """
    Set up the window with the given background color and title.
    Returns the new window.
    """

    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)

    return w


def make_turtle(color, size):
    """
    Set up a turtle with the given color and pensize.
    Returns the new turtle.
    """

    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t
