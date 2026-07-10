"""
Purpose:
Performs a basic exploratory data analysis using a CSV dataset.

The program:

- Reads a CSV file using Pandas.
- Calculates descriptive statistics (mean, median and standard deviation).
- Displays the calculated statistics in the console.
- Creates a scatter plot comparing Sales and Profit using Matplotlib.

This project was developed during the
"Cursor AI + Python: Intelligent Development with AI"
course provided by Santander Open Academy.
"""

import matplotlib.pyplot as plt  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]

# Read the CSV file named 'data.csv' into a pandas DataFrame
df = pd.read_csv("data.csv")

# Calculate descriptive statistics
mean = df.mean()
median = df.median()
std_dev = df.std()

print("Mean for each column:")
print(mean)

print("\nMedian for each column:")
print(median)

print("\nStandard deviation for each column:")
print(std_dev)

# Create scatter plot
plt.scatter(df["sales"], df["profit"])

plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit Scatter Plot")

plt.show()