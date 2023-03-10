#Download the file ""redundant2.csv"" from the repository "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/".
#Apply NMF and extract two its main features. Plot scatter plot for them.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF

# load the data
url = "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/redundant2.csv"
data = pd.read_csv(url)

# apply NMF with 2 components
nmf = NMF(n_components=2)
nmf_features = nmf.fit_transform(data)

    # plot scatter plot for the two main features
plt.scatter(nmf_features[:, 0], nmf_features[:, 1])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
