#Write a program that finds the minimum of the function
#f(x1,x2,x3) = 0.1x1e^x1+0.3x2e^x2+0.6x3e^x3 using a gradient descent.

import numpy as np

# Define the function to minimize
def f(x):
    x1, x2, x3 = x
    return 0.1*x1*np.exp(x1) + 0.3*x2*np.exp(x2) + 0.6*x3*np.exp(x3)

# Define the gradient of the function
def grad_f(x):
    x1, x2, x3 = x
    df_dx1 = 0.1*np.exp(x1)*(1+x1)
    df_dx2 = 0.3*np.exp(x2)*(1+x2)
    df_dx3 = 0.6*np.exp(x3)*(1+x3)
    return np.array([df_dx1, df_dx2, df_dx3])

# Define the gradient descent algorithm
def gradient_descent(x_start, learning_rate, num_iterations):
    x = x_start
    x_history = [x]
    for i in range(num_iterations):
        # Compute the gradient of the function at the current point
        grad = grad_f(x)
        # Update the current point using the gradient and the learning rate
        x -= learning_rate*grad
        # Append the new point to the history list
        x_history.append(x)
    return x, f(x), x_history

# Set the initial point, learning rate, and number of iterations
x_start = np.array([0, 0, 0])
learning_rate = 0.01
num_iterations = 1000

# Run the gradient descent algorithm
x_min, f_min, x_history = gradient_descent(x_start, learning_rate, num_iterations)

# Print the result
print("The minimum of the function is at x =", x_min, "and f(x) =", f_min)
