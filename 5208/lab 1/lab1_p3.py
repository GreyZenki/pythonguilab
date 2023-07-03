#imports math 
import math

#asks the user for the degree
degree = int(input("Enter degree:"))

#converts the degree to radians
radian = degree*(math.pi/180)

#gets the sin, cos, and tan of the radian
sin_r = math.sin(radian)
cos_r = math.cos(radian)
tan_r = math.tan(radian)

#prints the sin, cos, tan, and radian 
print("The sin of the degree is:", sin_r)
print("The cos of the degree is:", cos_r)
print("The tan of the degree is:", tan_r)
print("The degree converted to radian is:", radian)

#finds and prints the quadrant of the degree
if degree>=0 and degree<= 90:
    print("degree is in first quadrant")
elif degree<=90 and degree<=180:
    print("degree is in second quadrant")
elif degree<=180 and degree<=270:
    print("degree is in third quadrant")
else:
    print("degree is in fourth quadrant")    
    
