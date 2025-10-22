#functions are either void or fruitful 
# all import atatemnts are here 
import math

#All global variables are here
#Global Variability
#f_name = ""

#FUNCTION DECLARATIONS
#void function
#def setName(fname):
    #fname is the local function variable
    #f_name is global variable set above
     #f_name = fname
     
#print(fname)

#fruitful function
#def getName():
    #return f_name




#Function Call
#setName("Megan")
#setName("Amanda")
#setName("Tess")


#name = getName()
#print("Hi", name)



#def sum(numbers):
     #sum = 0 
     #for i in numbers (len(numbers)): #[1:len(numbers)]
          #sum += i # += is equivalent to sum = sum + i
          #return sum


#num1 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,10

#test1 = sum(num1)



#def absolute_value(x):
# if x < 0:
# return -x # the return statement exists the function
# else:
# return x

                  
#Testing Suite

#print(test1)

#Boolean Functions return a True or False calue 
#examples of boolean functions are:
# is age 16?
# is the password correct?

#Fun fact: Boolean functions are normally name is _____
#def isDivisible(x, 4):
     #if (x%y) == 0 
          #  return True
     #else: 
      #    return False
     

#a fruitful compare function that compares two integers 
# and returns the largest integers
def compare(num1, num2):
    if(num1>num2):
        return num1
    elif(num2>num1):
        return num2
    else:
        print("The numbers are equal")

print(compare(5, 10))

#a frutiful hypotenuse fucntion that returns the value of the hypotenuse given the a and b savlue.abs
def hypotenuse(a,b):
    c = math.sqrt(a**2 + b**2)
    return c
print(hypotenuse(3,4))



#a fruitful slope function that returns the slops of a line 
#given 4 parameters (x1, y1,x2,y2)
def slope(x1, y1, x2, y2):
    m=(y2 - y1) / (x2 - x1)
    return m 
print(slope(1,2,3,4))

#a fruitful intercept function that will find the y-intercept 
#given two points (x1, y1, x2, y2)
# ***This function should call the slope function in order to
#*** calculate the y-intercept of b-value
def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    b = y1 - (m * x1)
    return b
print(intercept(1,2,3,4))


#a fruitful function that will calculate whether a number is 
#a factor of another number.
#***Is 3 a factor of 9?
#** return a BOOLEAN (true or false)
def factor(factor, number):
    if (number % factor) == 0:
        return True
    else:
        return False
    print(factor(3,9))
#a frutiful function that will calculate whether a numbe is 
#a multiple of another number
#***Is 12 a mupltiple of 36?
#***retunrn a BOOLEAN (true or false)
def multiple(multiple, number):
    if (multiple % number) ==0:
        return True
    else:
        return False
    print(multiple(12,36))