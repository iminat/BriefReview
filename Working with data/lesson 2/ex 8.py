#Download the file "happiness_score.csv" from the repository
#"https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/".
#Rescale its column 'Happiness Score'. Transform its column 'Region' into one-hot representation.
#Compute pairwise distances using 'Happiness Score' and one-hot columns for 'Region'.
#Find two most similar countries.

import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/happiness_score.csv"
data = pd.read_csv(url)

# rescale the 'Happiness Score' column to the range [0, 1]
data['Happiness Score'] = (data['Happiness Score'] - data['Happiness Score'].min()) / (data['Happiness Score'].max() - data['Happiness Score'].min())

# transform the 'Region' column into one-hot representation
regions = pd.get_dummies(data['Region'], prefix='Region')
data = pd.concat([data, regions], axis=1)

# compute pairwise distances using 'Happiness Score' and one-hot columns for 'Region'
distances = np.zeros((data.shape[0], data.shape[0]))
for i in range(data.shape[0]):
    for j in range(i+1, data.shape[0]):
        dist_score = np.abs(data.loc[i,'Happiness Score'] - data.loc[j,'Happiness Score'])
        dist_region = np.sum(np.abs(data.loc[i,'Region_Africa':'Region_Western Europe'] - data.loc[j,'Region_Africa':'Region_Western Europe']))
        distances[i,j] = np.sqrt(dist_score**2 + dist_region**2)
        distances[j,i] = distances[i,j]

# find the two most similar countries
similarities = np.argsort(distances[0,:])[1:3]
print(data.loc[similarities, 'Country'])
