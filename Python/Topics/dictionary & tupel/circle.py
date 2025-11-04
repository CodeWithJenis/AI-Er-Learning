''' Write circle_calc() function that takes radius of a circle as an input from user and then it calculates
 and returns area, circumference and diameter. You should get these values in your main program by calling
 circle_calc function and then print them '''
import math
def circle_calc(radius):
    area = radius * radius * math.pi
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter

radius = float(input("Enter radius: "))
d=circle_calc(radius) #tupel value stored
print(d)

