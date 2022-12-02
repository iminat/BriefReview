#Write a program that creates a NumPy array  containing 11 equally spaced values from 0 to .
#Now compute two new arrays:  and .
#Finally compute and print the result of expression

import numpy as np

x = np.linspace(0, 2*np.pi, 11)
s = np.array(np.sin(x))
c = np.array(np.cos(x))
print(s**2+c**2)