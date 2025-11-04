'''Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width If no shape is supplied then it should take triangle as a default shape '''

def area(base,height,shapetype="triangle"):
    if(shapetype == "triangle"):
        return 0.5*base*height
    else:
        return base*height
result = area(2,3)
print(result)