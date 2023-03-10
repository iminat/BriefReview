#Download the file "rescale.csv" from the repository "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/"
#Rescale its columns, compute all pairwise distances and find three closest records.
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/rescale.csv"
data = pd.read_csv(url)

# rescale the data columns to the range [0, 1]
data_scaled = (data - data.min()) / (data.max() - data.min())

# compute the pairwise distances between records
distances = np.zeros((data.shape[0], data.shape[0]))
for i in range(data.shape[0]):
    for j in range(i+1, data.shape[0]):
        distances[i,j] = np.linalg.norm(data_scaled.iloc[i,:] - data_scaled.iloc[j,:])
        distances[j,i] = distances[i,j]

# find the three closest records for each record
closest_records = np.zeros((data.shape[0], 3), dtype=int)
for i in range(data.shape[0]):
    closest_records[i,:] = np.argsort(distances[i,:])[1:4]

print(closest_records)

