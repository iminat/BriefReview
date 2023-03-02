import numpy as np
import pandas as pd

# Load data into a pandas DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/bank_customers.csv")

# Extract the "Months" column as a NumPy array
months = df['Months'].to_numpy()

# Calculate mean
mean = np.mean(months)

# Calculate median
median = np.median(months)

# Calculate mode
(values, counts) = np.unique(months, return_counts=True)
mode = values[np.argmax(counts)]
import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram(data, column):
    # Load data into a pandas DataFrame
    df = pd.read_csv(data)

    # Extract the specified column as a NumPy array
    column_data = df[column].to_numpy()

    # Plot the histogram
    plt.hist(column_data, bins=50, edgecolor='black')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column}')
    plt.show()

# Call the function to plot the histogram of the "Months" column
plot_histogram("https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/bank_customers.csv", "Months")