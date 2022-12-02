# Write a program that creates a NumPy array containing 20 zeros,
# then reshape it to get a two-dimensional array with 5 rows and 4 columns.
# Print this array.
# Now assign to its middle area 1 to obtain an array whose the first and the last rows
# as well as the first and the last columns contain 0 and all others are 1.
# Print this array.

import numpy as np
c = np.zeros(20).reshape(5,4)
print(c)
c[1][1:3] = 1
c[2][1:3] = 1
c[3][1:3] = 1
print(c)