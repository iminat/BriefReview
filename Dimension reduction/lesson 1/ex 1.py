#Download the file ""redundant1.csv"" from the repository "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/".
# Apply PCA to reveal its number of essential features.Compute the reduced dataset and create a scatter plot for it

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Downloading the data
url = 'https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/redundant1.csv'
data = pd.read_csv(url)

# Separating the features from the target variable
X = data.drop('class', axis=1).values

# Applying PCA to determine the number of essential features
pca = PCA()
pca.fit(X)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')
plt.show()

# From the plot, we can see that the first 2 components explain most of the variance
n_components = 2

# Computing the reduced dataset
pca = PCA(n_components=n_components)
X_reduced = pca.fit_transform(X)

# Creating a scatter plot of the reduced dataset
colors = ['blue', 'red']
for i, target_name in enumerate(set(data['class'])):
    plt.scatter(X_reduced[data['class']==target_name,0], X_reduced[data['class']==target_name,1], label=target_name, color=colors[i])
plt.legend()
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
