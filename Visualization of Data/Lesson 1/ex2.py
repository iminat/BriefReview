# Total energy supply (TES) by source, World 2015
# Unit of measurement: Thousand tons of oil equivalent (ktoe)
# ["Coal", "Natural gas", "Nuclear", "Hydro", "Wind, solar, etc", "Biofuels and waste", "Oil"]
# dat = [3842742, 2928795, 670172, 334851, 203821, 1271235, 4328233]
# Above is the dataset describing world total energy supply recorded at 2015.
# Create a bar plot for it.Write text labels with values on each bar.Add x and y axes labels.

energy = ["Coal", "Natural gas", "Nuclear", "Hydro", "Wind, solar, etc", "Biofuels and waste", "Oil"]
dat = [3842742, 2928795, 670172, 334851, 203821, 1271235, 4328233]

import matplotlib.pyplot as plt
import numpy as np

# Creating a simple bar chart
# Increase the size of the figure (chart)
plt.figure(figsize=[8, 8])

# Creating a bar chart with the parameters
plt.bar(energy, dat, width=0.5)
plt.xticks(energy, rotation=15)
plt.bar(energy, dat)


plt.title('Total energy supply by source, World 2015')
plt.xlabel('Type of energy', fontsize=12)
plt.ylabel('Thousand tons of oil equivalent (in ktoe)', fontsize=12)
plt.show()