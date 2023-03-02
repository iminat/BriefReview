#Write a program that finds the minimum of the function y(x)= 1-e^-(x-5)^2 using a gradient descent.

import numpy as np
import matplotlib.pyplot as plt

# Define the function to minimize
def y(x):
    return 1 - np.exp(-(x-5)**2)

# Define the derivative of the function
def dy_dx(x):
    return 2*(x-5)*np.exp(-(x-5)**2)

# Define the gradient descent algorithm
def gradient_descent(x_start, learning_rate, num_iterations):
    x = x_start
    x_history = [x]
    for i in range(num_iterations):
        # Compute the gradient of the function at the current point
        grad = dy_dx(x)
        # Update the current point using the gradient and the learning rate
        x -= learning_rate*grad
        # Append the new point to the history list
        x_history.append(x)
    return x, y(x), x_history

# Set the initial point, learning rate, and number of iterations
x_start = 0
learning_rate = 0.1
num_iterations = 100

# Run the gradient descent algorithm
x_min, y_min, x_history = gradient_descent(x_start, learning_rate, num_iterations)

# Print the result
print("The minimum of the function is at x =", x_min, "and y =", y_min)

# Plot the function and the gradient descent path
x = np.linspace(-10, 20, 1000)
plt.plot(x, y(x), label='y(x)')
plt.plot(x_history, y(np.array(x_history)), 'ro-', label='gradient descent')
plt.legend()
plt.show()
