import turtle


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
# koch(alex, 0, 100)
# koch(alex, 1, 100)
# koch(alex, 2, 100)
# koch(alex, 3, 300)
koch(alex, 4, 400)
wn.mainloop()
