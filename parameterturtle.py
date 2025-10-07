import turtle
screen = turtle.Screen()
screen.title("Turtle Parameter Example")
screen.bgcolor("pink")

poly = turtle.Turtle()
poly.shape("turtle")
poly.color("purple")

def draw_clock():
    poly.stamp()
    
    for i in range(12):
        
        poly.penup()
        poly.forward(150)
        poly.pendown
        poly.stamp()
        poly.penup()
        poly.backward(150)
        poly.left(30)


def draw_multicolor_square(t, sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)






#TEST SUITE
def test():
    test_turtle = turtle.Turtle()
    test_turtle.color("pink")
    #draw_clock() #without a parameter
    #draw_clock(test_turtle) #with a turtle parameter
    draw_multicolor_square(test_turtle, 20)
    draw_multicolor_square(test_turtle, 50)
    draw_multicolor_square(test_turtle, 100)



    
turtle.done()
screen.listen()
screen.mainloop()


