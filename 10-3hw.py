"""Write a void (non-fruitful) function to draw a square. 
Use it in a program to draw the image shown below. Assume each side is 20 units"""
import turtle 

screen = turtle.Screen()
screen.title("Clock Turtle")
screen.bgcolor("lightgreen")

poly = turtle.Turtle()
poly.shape("turtle")
poly.color("blue")
poly.pensize(3)
poly.speed(450)
poly.shape("arrow")
poly.color("hotpink")

def draw_square(t, side):
    poly.pendown()
    for i in range(4):
        poly.forward(20)
        poly.right(90)
def draw_multiple_squares(t, side, num):
    for i in range(num):
        draw_square(t, side)
        poly.penup()
        poly.forward(side)
        poly.pendown()

draw_square()
screen.listen()
screen.mainloop()

