#Download the dataset from the previous exercise and do the same as in the exercise 1 for the column CredLim.
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
data_grd = [int(s[2]) for s in lst_data]
print(data_grd[:10])

#data size and largest and smallest units in data
print(f'Data size={len(data_grd)}')
print(f'Largest  month number={max(data_grd)}')
print(f'Smallest month number={min(data_grd)}')

#HISTOGRAM
#Since our data are integers we can compute an exact number of bins: one for each particular value.

def my_mean(data):
    """
    Mean value of dataset.
    """
    return sum(data) / len(data)
data_mean = my_mean(data_grd)
print(f'data_mean={data_mean}')


def my_median(data):
    """
    Median of a dataset.
    """
    size = len(data)
    srt_data = sorted(data)
    if size % 2 != 0:
        # odd length
        midpoint = size // 2
        return srt_data[midpoint]
    else:
        # even length
        hi_midpoint = size // 2
        lo_midpoint = hi_midpoint - 1
        return (srt_data[lo_midpoint] + srt_data[hi_midpoint]) / 2



from collections import Counter

def my_mode(data):
    """
    Returns a list of the most frequent elements
    """
    bins = Counter(data)
    most_freq = bins.most_common(1)[0][1]
    return [key for key, val in bins.items() if val == most_freq]
#my_mode(nums)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(data_grd, bins=max(data_grd) - min(data_grd) + 1);
ax.set_xlabel("CredLim")
ax.set_ylabel("# of customers")

data_mean = my_mean(data_grd)
data_median = my_median(data_grd)
data_mode = my_mode(data_grd)

print(f"mean   = {data_mean:5.2f}")
print(f"median = {data_median}")
print(f"mode   = {data_mode}")

ax.axvline(data_mean, color='red', linewidth=3, label=f'mean at {data_mean:5.2f}')
ax.axvline(data_median, color='green', linewidth=3, label=f'median at {data_median}')

for md in data_mode:
    ax.axvline(md, color='cyan', linewidth=3, label=f'mode at {md}')

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


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(data_grd, bins=max(data_grd) - min(data_grd) + 1);
ax.set_xlabel("CredLim")
ax.set_ylabel("# of customers")

Q1 = my_quantile(data_grd, 0.25, reverse=True)
Q2 = my_median(data_grd)
Q3 = my_quantile(data_grd, 0.75, reverse=True)

ax.axvline(Q1, color='C1', linewidth=3, label=f'Q1 at {Q1}')
ax.axvline(Q2, color='C2', linewidth=3, label=f'Q2 at {Q2}')
ax.axvline(Q3, color='C3', linewidth=3, label=f'Q3 at {Q3}')

ax.legend()
ax.grid()
plt.show()