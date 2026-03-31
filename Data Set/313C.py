import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv("student_data.csv")
df.columns = df.columns.str.strip()

data = df['How many hour do you study daily?']

# --- Calculate outliers using IQR ---
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = data[(data < lower_bound) | (data > upper_bound)]

# --- Plot ---
plt.boxplot(data)

# Highlight outliers manually
plt.scatter([1]*len(outliers), outliers, color='red', label='Outliers', zorder=3)

plt.title('Study Hours Distribution with Outliers')
plt.ylabel('Study Hours')

plt.legend()
plt.show()

# Print outliers
print("Outliers:\n", outliers.values)