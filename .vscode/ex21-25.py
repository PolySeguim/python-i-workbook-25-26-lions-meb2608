"""
Exercise 21: Area of a Triangle
The area of a triangle can be computed using the following formula,
where b is the length of the base of the triangle, and h is its
height:
area = (b*h)/2
Write a program that allows the user to enter values for b and h.
The program should then compute and display the area of a triangle
with base length b and height h
"""
def areaTriangle():
    b = int(input("What is the base of the triangle? "))
    h - int(input("What is the height of the triangle? "))
    area = (b*h)/2  
    print("The area of the triangle is" +str(area))
"""
Exercise 22: Area of a triangle (Again)
In the previous exercise you created a program that computed the area
of a triangle when the length of its base and its height were known.
It is also possible to compute the area of a triangle when the lengths
of all three sides are known. Let s1, s2, and s3 be the lengths of the
sides. Let s = (s1 + s2 + s3)/2. Then the area of a triangle can be
calculated using the following formula:
area = (s * (s - s1) * (s - s2) * (s - s3))**(1/2)
Develop a program that reads the lengths of the sides of a triangle from
the user and display its area.
"""
def areaTriangleagain():
    s1 = float(input("What is the length of side 1? "))
    s2 = float(input("What is the length of side 2? "))
    s3 = float(input("What is the length of side 3? "))
    s = (s1 + s2 + s3)/2
    area = (s * (s - s1) * (s - s2) * (s - s3))**(1/2)
    print("The area of the triangle is " + str(round(area,2)))

"""
Exercise 23: Area of a Regular Polygon
A polygon is regular if its sides are all the same length and the angles
between all of the adjacent sides are equal. The area of a regular polygon
can be computed using the following formula, where s is the length of a side
and n is the number of sides:
area = (n * s**(2))/(4 * tan(pi/n))
Write a program that reads s and n from the user and then displays the area
of a regular polygon constructed from these values.
"""
def areaRegularPolygon():
    import math
    s = float(input("What is the length of a side? "))
    n = int(input("What is the number of sides? "))
    area = (n * s**(2))/(4 * math.tan(math.pi/n))
    print("The area of the regular polygon is " + str(round(area,2)))
"""
Exercise 24: Units of Time
Create a program that reads a duration from the user as a number of days,
hours, minutes, and seconds. Compute the total number of seconds represented
by this duration.
"""
def unitsoftime():
    days = int(input("Enter number of days: "))
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
    print("The total number of seconds is " + str(total_seconds))
"""
Exercise 25: Units of Time (again)
In this exercise you will reverse the process described in the previous
exercise. Develop a program that begins by reading a number of seconds from
the user. Then your program should display the equivalent amount of time
in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours,
minutes and seconds respectively. The hours, minutes and seconds should all
be formatted so that they occupy exactly two digits, with a leading 0 displayed
if necessary.
"""
def unitsoftimeagain():
    totalseconds = int(input("What is the total number of seconds?"))
    days = totalseconds // 86400
    remainingseconds = totalseconds % 86400
    hours = remainingseconds // 3600
    remainingsecondss = hours % 3600
    minutes = remainingsecondss // 60
    remaindingsecondsss = minutes % 60
    seconds = remaindingsecondsss // 1
    print(str(days) + ":" + str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))

#Testing Suite
#areaTriangle()
#areaTriangleagain()
#areaRegularPolygon()
#unitsoftime()
unitsoftimeagain()



