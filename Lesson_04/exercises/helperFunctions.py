from turtle import Screen, Turtle


def make_window(color: str, title: str) -> Screen:
    """
    Creates a window with the specified color and title.

    Args:
        color (str): The color of the window.
        title (str): The title of the window.

    Returns:
        Screen: The created window.

    Example:
    ```python
    color = "blue"
    title = "My Window"
    window = make_window(color, title)
    window.mainloop()
    """
    w = Screen()
    w.bgcolor(color)
    w.title(title)

    return w


def make_turtle(color: str, size: int) -> Turtle:
    """
    Creates a turtle with the specified color and size.

    Args:
        color (str): The color of the turtle.
        size (int): The size of the turtle's pen.

    Returns:
        Turtle: The created turtle.

    Example:
    ```python
    color = "red"
    size = 2
    turtle = make_turtle(color, size)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.mainloop()
    """
    t = Turtle()
    t.color(color)
    t.pensize(size)
    return t
