import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read data from a CSV file
data = pd.read_csv('data.csv')

# Perform data manipulation with Pandas
filtered_data = data[data['column_name'] > 10]
grouped_data = data.groupby('category').mean()

# Perform data analysis
mean_value = np.mean(data['column_name'])
max_value = np.max(data['column_name'])

# Create a line plot
plt.plot(data['x'], data['y'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()
