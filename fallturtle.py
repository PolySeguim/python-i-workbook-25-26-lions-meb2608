import turtle

# Create a turtle object - complex data type
megan = turtle.Turtle()
megan.color("blue")
megan.shape("turtle")

#Screen is a complex data type - has attributes and behaviors
screen = turtle.Screen()
screen.title

def square():
    for i in range(4):
        megan.forward(100)
        megan.right(90)

def pentagon():
    for i in range(5):
        megan.forward(100)
        megan.right(72)

def rainbow():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
        megan.color(color)
        megan.forward(10)
        megan.circle(20)
        megan.forward(10)

def backForth():
    megan.speed(1)
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
        megan.color(color)
        megan.pensize(4)
        megan.forward(100)
        megan.forward(-50)

def funActivity():
    size = 20
    for i in range(30):
        megan.stamp()
        size = size + 3
        megan.penup()
        megan.forward(size)
        megan.pendown()
        megan.right(24)

def classTwo():
    length = 5
    megan.speed(10)
    for i in range(200):
        megan.forward(length)
        megan.right(90)
        length = length + 3

def classThree():
    length = 5
    megan.speed(10)
    for i in range(200):
        megan.forward(length)
        megan.left(91)
        length = length + 3

def pythonTurtles():
    for i in range(10): # for 1000 times, I would switch the 10 to 1000. i just don't want to print it that many times
        print("We like Python's turtles!")

def months():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for month in months:
        print("One of the months of the year is " + month)

def iterationExercise():
    xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    sum = 0
    product = 1
    for number in xs:
        sum = sum + number
        product = product * number
        print(number, " -- ", number**2)
        print(sum, product)

def clock(t):
    t.shape("turtle")
    screen.bgcolor("green")
    for i in range(12):
        t.penup()
        t.forward(100)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.stamp()
        t.penup()
        t.forward(-10)
        t.pendown()
        t.forward(-10)
        t.penup()
        t.forward(-100)
        t.right(30)

#test suite
def test():
    color1 = ["red", "purple", "hotpink", "blue", 2]
    color2 = ["black", "orange", "green", "yellow", 3]
    color3 = ["purple", "pink", "orange", "red ", 4]
    t = turtle.Turtle()
    multiColorSquare(t, 100, color1, 5)
    multiColorSquare(t, 50, color2, 10)
    multiColorSquare(t, 75, color3, 15)

def multiColorSquare(t, sz, colors, width):
    for i in colors:
        t.forward(sz)
        t.left(90)
        t.color(i)
        t.pensize(width)

def getThickness():
    thickness = int(input("Enter the thickness of the turtle"))
    return thickness

def firstSquare():
    for i in range(5):
        for i in range(4):
            megan.forward(20)
            megan.left(90)
        megan.penup()
        megan.forward(40)
        megan.pendown()

def secondSquare():
    length = 20
    for i in range(5):
        megan.penup()
        megan.forward(length / 2)
        megan.right(90)
        megan.forward(-(length / 2))
        megan.pendown()
        for i in range(4):
            megan.forward(length)
            megan.right(90)
        length = length + 20
        megan.penup()
        megan.goto(0, 0)

#screen.onkey(square, "k")
#screen.onkey(pentagon, "l")
#screen.onkey(foward100, "Up")
#screen.onkey(right90, "Right")
#screen.onkeypress(circle, "Left")
#screen.listen()
#screen.mainloop()
#rainbow()
#backForth()
#funActivity()
#pythonTurtles()
#months()
#iterationExercise()
#inClass()
#classTwo()
#classThree()
#test()
#firstSquare()
secondSquare()


# Keep the window open until clicked
turtle.done()
screen.listen()
screen.mainloop()