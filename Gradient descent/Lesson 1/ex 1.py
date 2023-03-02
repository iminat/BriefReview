#For the functions y(x) listed below compute the derivatives at x:
#y(x) = 2x^2 - x
#y(x) = sin x^2
#y(x) = e^-3x
#y(x) = log(1/x)

import numpy as np

# Define the functions
def y1(x):
    return 2*x**2 - x

def y2(x):
    return np.sin(x**2)

def y3(x):
    return np.exp(-3*x)

def y4(x):
    return np.log(1/x)

# Define the value of x at which to compute the derivatives
x = 2

# Compute the step size for finite differences
h = 1e-6

# Compute the derivatives using finite differences
dy1 = (y1(x + h) - y1(x - h)) / (2*h)
dy2 = (y2(x + h) - y2(x - h)) / (2*h)
dy3 = (y3(x + h) - y3(x - h)) / (2*h)
dy4 = (y4(x + h) - y4(x - h)) / (2*h)

# Print the results
print("The derivatives of the functions are:")
print("y1'(x) =", dy1)
print("y2'(x) =", dy2)
print("y3'(x) =", dy3)
print("y4'(x) =", dy4)
