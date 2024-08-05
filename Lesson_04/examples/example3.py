def draw_rectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)


def draw_square(t, sz):
    draw_rectangle(t, sz, sz)
