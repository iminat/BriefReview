#Download the file "skewed_data_1d.txt" from the repository "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/".
#This file contains one column of data. Describe it using corresponding function from the module scipy.stats.
#Analyze its skewness and kurtosis. What can you say about the dataset based on these values? Plot a histogram.

import numpy as np

url = "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/skewed_data_1d.txt"
data = np.loadtxt(url)

from scipy.stats import skew, kurtosis
skewness = skew(data)
kurtosis_val = kurtosis(data)

import matplotlib.pyplot as plt
plt.hist(data, bins=20, density=True)
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Histogram of Skewed Data")
plt.show()

import numpy as np
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/skewed_data_1d.txt"
data = np.loadtxt(url)

skewness = skew(data)
kurtosis_val = kurtosis(data)

plt.hist(data, bins=20, density=True)
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Histogram of Skewed Data")
plt.show()

print("Skewness:", skewness)
print("Kurtosis:", kurtosis_val)

