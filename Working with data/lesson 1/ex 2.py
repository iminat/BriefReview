#Download the file "multidim_corr.csv" from the repository "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/".
#This file contains several columns of data. Plot pairwise scatter plots as well as separated histograms.
#Compute the correlation matrix.
#What can you say about the dependencies between the data columns?

import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/multidim_corr.csv"
data = pd.read_csv(url)
from pandas.plotting import scatter_matrix

scatter_matrix(data, alpha=0.7, figsize=(8, 8), diagonal="hist")
plt.show()

corr_matrix = data.corr()
print(corr_matrix)
