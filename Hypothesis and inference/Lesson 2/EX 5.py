#Compute the mean and 95 % confidence interval for 400 heads in a series of 1000 tossing of a coin.

import numpy as np

# Parameters
n = 1000
p = 0.5
x = 400

# Compute the mean and standard error
mean = n * p
std_error = np.sqrt(n * p * (1 - p))

# Compute the 95% confidence interval
conf_int = (mean - 1.96 * std_error, mean + 1.96 * std_error)

print(f"The mean is: {mean:.2f}")
print(f"The 95% confidence interval is: [{conf_int[0]:.2f}, {conf_int[1]:.2f}]")
