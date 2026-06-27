import math

"""
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

# The radius of a circle is 30 meters. Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = int(input("Enter the radius: "))
area_of_circle = math.pi * (radius**2)
print(f"This is the area: {area_of_circle}")

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*math.pi*radius
print(f"This is the circumference is {circum_of_circle}")

# Run help("keywords")
help("keywords")