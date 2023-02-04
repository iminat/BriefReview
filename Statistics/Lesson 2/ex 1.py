#File "bank_customers.csv" that you can find at "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/"
# describes bank clinets.
# It contains three columns: customer age (CustAge),
# period of relationship with the bank in months (Months), and credit limit (CredLim).
# Plot a histogram for the column CustAge and compute its standard deviation
# and the interquartile range.
# Show them on the plot.
import requests

# This is an URL of a repository
base_url = "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/"
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
# Take only months
data_grd = [int(s[0]) for s in lst_data]
print(data_grd[:10])

#data size and largest and smallest units in data
print(f'Data size={len(data_grd)}')
print(f'Largest  month number={max(data_grd)}')
print(f'Smallest month number={min(data_grd)}')


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

#print(my_stddev(tst_data))

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(data_grd, bins=max(data_grd) - min(data_grd) + 1);
ax.set_xlabel("# of raised hand")
ax.set_ylabel("# of students")

data_mean = my_mean(data_grd)
data_std = my_stddev(data_grd)

ax.axvline(data_mean, color='red', linewidth=3, label=f'mean at {int(data_mean)}')
ax.axvspan(-data_std + data_mean, data_std + data_mean, color='yellow', alpha=0.3, label=f'$\sigma={data_std:4.2f}$')
ax.legend()
ax.grid()
plt.show()


def my_quantile(data, q, reverse=False):
    """
    The quantile, q in (0,1)
    reverse=True means sorting the array in descending order
    """
    inx = int(round(q * len(data)))
    return sorted(data, reverse=reverse)[inx]
def my_interquart(data):
    return my_quantile(data, 0.75) - my_quantile(data, 0.25)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(data_grd, bins=max(data_grd) - min(data_grd) + 1);
ax.set_xlabel("Total grade")
ax.set_ylabel("# of applicants")

data_mean = my_mean(data_grd)
data_std = my_stddev(data_grd)
ax.axvspan(-data_std + data_mean, data_std + data_mean, color='yellow', alpha=0.3, label=f'$2\sigma={2*data_std:4.2f}$')

Q1 = my_quantile(data_grd, 0.25)
Q3 = my_quantile(data_grd, 0.75)
ax.axvspan(Q1, Q3, color='gray', alpha=0.3, label=f'iqr={Q3-Q1:4.2f}')

ax.legend()
ax.grid()
plt.show()
