import turtle 
screen = turtle.Screen()
screen.title("Clock Turtle")
screen.bgcolor("white")
spiral= turtle.Turtle()
spiral.shape("turtle")
spiral.color("pink")

def draw_spiral():
   spiral.speed(450)
   length = 5 
   spiral.pendown()
   spiral.left(270)
   spiral.forward(length)
   for i in range(200):
        spiral.right(91)
        spiral.forward(length)
        length = length + 3
    



draw_spiral()



screen.listen()
screen.mainloop()