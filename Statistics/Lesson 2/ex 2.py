# Download the dataset from the previous exercise
# and compute correlation coefficients for each pair of columns.
import requests
# This is an URL of a repository
base_url = "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/"
# We need this file
file_name = "bank_customers.csv"
# Here we download the file
web_data = requests.get(base_url + file_name)
assert web_data.status_code == 200

# Take a look at the data
print(web_data.text[:100])
# Split by line ends
str_data = web_data.text.splitlines()
print(str_data[:10])
# Drop out the header and split grades
lst_data = [s.split(',') for s in str_data[1:]]
print(lst_data[:10])

# Take all 3 columns
data_pml = [[int(s[0]), int(s[1]), int(s[2])] for s in lst_data]
print(data_pml[:10])

import numpy as np
rng = np.random.default_rng()

xs = rng.integers(10, size=1000)
ys = rng.integers(100, size=1000)
def my_mean(data):
    """
    Mean value of dataset.
    """
    return sum(data) / len(data)

def my_stddev(data):
    """
    Standard deviation.
    """
    size = len(data)
    mean = sum(data) / size
    sqr_dev = [(x - mean)**2 for x in data]
    variance = sum(sqr_dev) / (size - 1)
    return variance**0.5


def my_corrcoef(xs, ys):
    """
    Pearson correlaton coefficient
    """
    x_mean = my_mean(xs)
    y_mean = my_mean(ys)
    x_std = my_stddev(xs)
    y_std = my_stddev(ys)
    xd = [x - x_mean for x in xs]
    yd = [y - y_mean for y in ys]
    dot = [x * y for x, y in zip(xd, yd)]
    cov = sum(dot) / (len(dot) - 1)
    return cov / (x_std * y_std)

print(my_corrcoef(xs, ys))

# Compute correlations
cor = my_corrcoef([x[0] for x in data_pml], [x[1] for x in data_pml])
print(f"Phys-Math grades correlation {cor:5.2f}")

cor = my_corrcoef([x[0] for x in data_pml], [x[2] for x in data_pml])
print(f"Phys-Lang grades correlation {cor:5.2f}")

cor = my_corrcoef([x[1] for x in data_pml], [x[2] for x in data_pml])
print(f"Lang-Math grades correlation {cor:5.2f}")