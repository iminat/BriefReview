#Compute gradients of the following functions:

#f(x,y) = x^3 - y^2
#f(x,y) = sin(x+y)
#f(x,y) = xe^y

import numpy as np

# Define the functions
def f1(x, y):
    return x**3 - y**2

def f2(x, y):
    return np.sin(x+y)

def f3(x, y):
    return x*np.exp(y)

# Define the gradient functions
def grad_f1(x, y):
    return np.array([3*x**2, -2*y])

def grad_f2(x, y):
    return np.array([np.cos(x+y), np.cos(x+y)])

def grad_f3(x, y):
    return np.array([np.exp(y), x*np.exp(y)])

# Test the functions
x = 2
y = 3
print(grad_f1(x, y))
print(grad_f2(x, y))
print(grad_f3(x, y))
