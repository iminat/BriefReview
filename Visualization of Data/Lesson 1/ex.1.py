# Create a plot with graphs of two functions:  and .
# Add x and y axes labels and the legend. Turn on the grid. Customize curve colors and styles.

# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating vectors X and Y
x = np.linspace(-2, 2, 100)
y = np.exp(-x ** 2)
y2 = 3*x**2*y

fig, ax = plt.subplots()

# Label the axes
ax.set_xlabel('x')
ax.set_ylabel('y')

# Create the plot
ax.plot(x, y, ':m', label = '$e^{-x^2}$')
ax.plot(x,y2, '--k', label = '$3x^2e^{-x^2}$')

# Set the grid
ax.grid()
# Add the legend
ax.legend(loc = 'upper right')
# Show the plot
plt.show()





