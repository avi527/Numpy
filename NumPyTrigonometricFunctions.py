import numpy as np
#NumPy Trigonometric Functions – Np.Sin(), Np.Cos(), Np.Tan()

#NumPy Trigonometric Functions
'''NumPy supports trigonometric functions like sin, cos, and tan, etc. 
The NumPy trigonometric functions help
to solve mathematical trigonometric calculation in an efficient manner. '''

#Sine value of angle in degrees
angle=np.sin(90)
print("Sine value of angle 90 in degree = ",angle)

#Sine value of the angle in radians
'''
To get sine value of the angle in radians, need to multiply angle with np.pi/180.
np.pi = 3.14
'''
sin_90=np.sin(90*np.pi/180)
print("Sine value of angle 90 in radians = ", sin_90)

#np.cos() Trigonometric Function
'''
The np.cos() NumPy function help to find cosine value of the angle in degree and radian.
'''
cos_180=np.cos(180)
print("cos value of angle 180 in degree = ",cos_180)

cosRadian=np.cos(180*np.pi/180)
print("cos value of angle 180 in radians = ", cosRadian)


#np.tan() Trigonometric Function
'''
The np.tan() NumPy function help to find cosine value of the angle in degree and radian.
'''
tanAngle=np.tan(60)
print("tan value of angle 180 in degree = ",tanAngle)

tanRadian=np.tan(60*np.pi/180)
print("tan value of angle 180 in radians = ", tanRadian)

#Graphical Representation of Trigonometric sine Function
import numpy as np # import numpy package
import matplotlib.pyplot as plt # import matplotlib.pyplot package
x = np.arange(0, 3 * np.pi, 0.1) # create x array of angels from range 0 to 3*3.14
y = np.sin(x) # create y array of sine values of angles from x array
plt.plot(x, y) # plot grah 
plt.title(" Graphical Representation of sine function")
plt.xlabel("x axis ")
plt.ylabel("y axis ")
plt.show() # show plotted graph







