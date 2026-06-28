# This script reads a CSV file, calculates statistics, and creates a scatter plot.

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file named 'data.csv' into a pandas DataFrame
df = pd.read_csv('data.csv')

# Calculate mean, median, and standard deviation for each column
mean = df.mean()
median = df.median()
std_dev = df.std()

# Print the calculated statistics with clear labels
print("Mean for each column:")
print(mean)
print("\nMedian for each column:")
print(median)
print("\nStandard deviation for each column:")
print(std_dev)

# Create a scatter plot of sales vs profit
plt.scatter(df["sales"], df["profit"])

# Label the axes
plt.xlabel("Sales")
plt.ylabel("Profit")

# Add a title to the chart
plt.title("Sales vs Profit Scatter Plot")

# Show the plot
plt.show()