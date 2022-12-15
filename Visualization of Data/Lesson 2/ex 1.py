# Create 3D surface plot of a function . Add axes labels and color bar.

def f(x,y):
    z = x**2 - y**2
    return z
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-5, 5, 101)
Y = np.linspace(-5, 5, 101)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

# {"projection": "3d"} activates using 3D plotting
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap='ocean')  # use fancy color map

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=20, pad=0.12);

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()