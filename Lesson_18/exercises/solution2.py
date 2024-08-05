import turtle


def cesaro(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [-80, 160, -80, 0]:
            cesaro(t, order - 1, size / 3)
            t.left(angle)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
cesaro(alex, 1, 100)
wn.mainloop()
