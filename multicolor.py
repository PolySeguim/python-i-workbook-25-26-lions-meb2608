import turtle


def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("black")

poly = turtle.Turtle()      # Create poly and set some attributes
poly.pensize(3)
poly.speed(1000)

size = 20                   # Size of the smallest square
for i in range(4000):
    draw_multicolor_square(poly, size)
    size = size + 10        # Increase the size for next time
    poly.forward(10)        # Move tess along a little
    poly.right(18)          #    and give her some turn

wn.mainloop()
