
"""
Exercise 16:  Area and Volume
Write a program that begins by reading a radius, r, from the user.  The program 
will continue by computing and displaying the area of a circle with radius r 
and the volume of a sphere with radius r.  Use the pi constant in the math 
module in your calculations.

Hint:  The are of  circle is computed using the formula area = pi*r**2.  The 
volume of a sphere is computed using the formula volume = 4/3 * pi * r**3.
"""
r = input(int("What is the radius in inches?"))
areaofcircle = 3.14 *r**2
volumeofsphere = 4/3 * 3.14 * r **3
print("Area of the circle =" (str(areaofcircle))
print("Volume of the sphere = " (str(volumeofsphere))
"""
Exercise 17:  Heat Capacity
The amount of energy required to increase the temperature of one gram of 
material by one degree Celsius is the material’s specific heat capacity, C.  
The total amount of energy required to raise m grams of a material by deltaT 
degrees Celsius can be computed using the formula:  q = mC deltaT.

Write a program that reads the mass of some water and the temperature change 
from the suer.  Your program should display the total amount of energy that 
must be added or removed to achieve the desired temperature change.

Hint:  The specific heat capacity of water is 4.186 J/gC.  Because water has 
a density of 1.0 gram per milliliter, you can use grams and milliliters 
interchangeably in this exercise.

Extend your program so that it also computes the cost of heating the water.  
Electricity is normally billed using units of kilowatt hours rather than Joules.  
In this exercise, you should assume that electricity costs 8.9 cents per 
kilowatt-hour.  Use your program to compute the cost of boiling water for 
a cup of coffee.

Hint:  You will need to look up the factor for converting between Joules 
and kilowatt hours to complete the last part of this exercise.
(25 lines)
"""
massofwater= input(int("What is the mass of water in grams? "))
temperaturechange = input(int("What is the temperature change in Celcius? "))
specificheatcapacity = 4.186
energyrequired = massofwater * specificheatcapacity * temperaturechange
costofelectricityperkwh = 0.089
joulesperkwhr = 3600000 
costofheating = (energyrequired / joulesperkwhr) * costofelectricityperkwh
print("The total amount of energy required is " + str(energyrequired) + " Joules")
print("The cost of heating the water is $" + str(costofheating))        

"""
Exercise 18:  Volume of a Cylinder
The volume of a cylinder can be computed by multiplying the area of its 
circular base by its height.  Write a program that reads the radius of the 
cylinder, along with its height, from the user and computes its volume.  
Display the result rounded to one decimal place.
(15 lines)
"""
radius = input(int("What is the radius of the cylinder in inches? "))
height = input(int("What is the height of the cylinder in inches? "))
cylindervolume = 3.14 *radius**2 * height
print("The volume of the cylinder is " + str(round(cylindervolume,1)) + " cubic inches")


"""
Exercise 19:  Free Fall
Create a program that determines how quickly an object is traveling when it 
hits the ground.  The user will enter the height from which the object is 
dropped in meters (m).  Because the object is dropped its initial speed is 
0 m/s.  Assume that the acceleration due to gravity is 9.8 m/s**2.  You can 
use the formula vf = (vi**2 + 2ad)**(1/2) to compute the final speed vf, 
when the initial speed, vi, acceleration, a, and distance, d, are known.
(16 lines)
"""
height = input(int("What is the height in meters that the object is dropped from? "))
initialspeed = 0 
acceleration = 9.8
finalspeed = (initialspeed**2 + 2*acceleration*height)**(1/2)
print("The final speed of the object when it hits the ground is " + str(finalspeed) + " m/s")


"""
Exercise 20: Ideal Gas Law
The ideal gas law is a mathematical approximation of the behavior of gasses as 
pressure, volume and temperature change.  It is usually stated as:

PV = nRT

Where P is the pressure in Pascals, V is the volume in liters, n in the amount 
of substance in moles, R is the ideal gas constant, equal to 8.314 J/molK, and 
T is the temperature is Kelvin.

Write a program that computes the amount of gas in moles when the user supplies 
the pressure, volume and temperature.  Test your program by determining the 
number of moles of gas in a SCUBA tank.  A typical SCUBA tank holds 12 liters 
of gas at a pressure of 20,000,000 Pascals (approximately 3,000 PSI).  
Room temperature is approximately 20 degrees Celsius or 68 degrees Fahrenheit.

Hint:  A temperature is converted from Celsius to Kelvin by adding 273.15 to it.  
To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it, multiply 
by 5/9 and then add 273.15 to it.

(19 lines)
"""
pressure = input(int("What is the pressure in Pascals? "))
volume = input(int("What is the volume in liters? "))
temperaturecelsius = input(int("What is the temperature in Celsius? "))
temperaturekelvin = temperaturecelsius + 273.15
R = 8.314
n = (pressure * volume) / (R * temperaturekelvin)
print("The amount of gas in moles is " + str(n) + " moles")
"""

if __name__ == "__main__":
    print("Hi there!")