"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of  the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""
mealcost = int(input("What is the cost of your meal?"))
taxrate = 0.067
tip = 0.18
mealtax = 0 
mealtax = mealcost * taxrate 
mealtip = 0
mealtip = mealcost * tip
totalcost = 0
totalcost = mealtax + mealtip + mealcost
print(totalcost)
"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""
n = int(input("Write a positive integer "))
sum = (n*(n+1))/2
print("Here's the sum" + str(sum)) 
"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)

"""
widgetweight = 75 
gizmoweight = 112
howmanywidgets = int(input("How many widgets do you have? "))
howmanygizmos = int(input("How many gizmos do you have? "))
totalweight = (widgetweight * howmanywidgets) + (gizmoweight * howmanygizmos)
print("The total weight is " + str(totalweight) + " grams")

"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""
interest = 0.04
balance = int(input("What is your bank balance? "))
print("This is your balance:" , balance)
balanceafter1year = balance + (balance * interest)
balanceafter2year = balance + (balanceafter1year * interest)
balanceafter3year = balance + (balanceafter2year * interest)
print("Balance after one year = " , balanceafter1year)
print("Balance after two years = " , balanceafter2year)
print("Balance after three years = " , balanceafter3year)
"""
Exercise 10:  Arithmetic
Create a program that reads two integers, a and b, from the user.  Your program
should compute and display:
- the sum of a and b
- the difference when b is subtracted from a
- the product of a and b
- the quotient when a is divided by b
- the remainder when a is divided by b
- the result of log10 a
- the result of a to the power of b

Hint:  you will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
import math
a = int(input("Whats the first integer? "))
b = int(input("What is the second integer? "))
sumab = a + b
difference = b-a
product = a * b
quotient = a/b
remainder = a % b 
log = math.log10(a)
power = a^b
print("The sum of" + str(a) + "and of" + str(b) + "=" + str(sumab))
print("The difference of" + str(b) + "and of" + str(a) + "=" + str(difference))
print("The product of" + str(a) + "and of" + str(b) + "=" + str(difference))
print("The quotient of" + str(a) + "and of" +str(b) + "=" + str (quotient))
print("The remainder of" + str(a) + "divided by" +str(b) +"=" +str(remainder))
print("The log10 of a =" + str(log))
print(str(a) + "to the power of" + str(b) + "="+  str(power))
if __name__ == "__main__":
    print("Hi there!")
