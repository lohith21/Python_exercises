import sys

## print pythong version
print("Python Version", sys.version)


## Pring current date and time in a specific format
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
now = datetime.datetime.now()
print(now)

### calculate area of a circle based on radius entered by user
from math import pi
#r = float(input ("Input the radius of the circle : "))
#print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
r = 3
print(pi * r**2)