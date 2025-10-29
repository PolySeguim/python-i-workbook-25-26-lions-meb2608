import turtle 
megan = turtle.Turtle()
megan.color("blue")
megan.shape("turtle")
screen = turtle.Screen()
screen.title




#Question 1-
#I got this question right YAY
def truth(a, b, c):
    if(a and (b or c)):
        return True
    return False
print(truth(False, False, False))   
print(truth(False, False , True))
print(truth(False, True, True))
print(truth(False, True, True))
print(truth(True , False , False))
print(truth(True, False, True))
print(truth(True, True, False))
print(truth(True, True, True))



#Question 2-
#I got this question wrong i hated my answer I wasn't thinking straight :(

import math    #i imported math this time so i could use pi 
radius = float(input("What is the radius of the circle? ")) #on my test I made it an integer instead of a float
def calculate_area(radius): #I also called and returned the function
    return math.pi * radius ** 2
print("The area of the circle is:", calculate_area(radius)) 

#Question 3-
#I have apsolutely no idea how to do this question. 
password = "1234"
i = input("What is the password? ")
if (i == password): 
    for i in range (3):
        print("You have succesfully logged in.")
else: 
    print("You have been denied access 2 tries remaining.")
    i2 = input("What is the password? ")
    if (i2 == password):
        print("You have succesfully logged in.")
    else:
        print("You have been denied access 1 tries remaining.")
        i3 = input("What is the password? ")
        if (i3 == password):
            print("You have succesfully logged in.")
        else:
            print("Access denied.")

#Question 4-
#I got this question right 

#Question 5- 
#I got the first two wrong and the rest right
    """== means
        Equals To

    != means
        Not equal to 
    > means 
        greater than 
    < means 
        less than 
    >= means
        greater than or equal to
    <= means 
        less than or equal to 
    """

#Question 6-
#I got this question right 
for i in [12, 16, 17,24,29]:
    if i % 2 == 1:
        break 
    print(i)
    print("done")

#Question 7-
#I got this question right
for i in [12, 16, 17,24,29, 30]:
    if i % 2 == 1:
        continue
    print(i)
    print("done")

#Question 8- 
#I got this question right, the syntax error is that there are no parentheses

#Question 9- 
#I got this question wrong.
#I put that its a line and its a square
def square(t, side):
    for i in range(4):
        megan.forward(side)
        megan.right(90)
def functionA(t, side, num):
    for i in range(num):
        square(t, side)
        megan.penup()
        megan.forward(side * 10)
        megan.pendown()
#functionA()
turtle.done()
screen.listen()
screen.mainloop()
#Question 10-
#I got this question right
def functionB():
    for i in range(5):
        megan.forward(100)
        megan.right(72)
functionB()
turtle.done()   









