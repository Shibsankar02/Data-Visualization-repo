import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_data.csv")
df.columns = df.columns.str.strip()

# Base variables from dataset
x = df['How many hour do you study daily?'].values
y = df['How many hour do you spent daily on your skill development?'].values

# --- Create positive correlation ---
y = x * 0.8 + np.random.normal(0, 0.5, len(x))

# --- Create clusters ---
# Cluster 1 (low values)
cluster1_x = x[:10] + np.random.normal(0, 0.2, 10)
cluster1_y = y[:10] + np.random.normal(0, 0.2, 10)

# Cluster 2 (high values)
cluster2_x = x[10:20] + 2
cluster2_y = y[10:20] + 2

# Combine clusters
X = np.concatenate([cluster1_x, cluster2_x])
Y = np.concatenate([cluster1_y, cluster2_y])

# --- Add outliers ---
X = np.append(X, [0.5, 6])
Y = np.append(Y, [6, 0.5])

# --- Plot ---
plt.scatter(X, Y, color='blue')

plt.title('Scatter Plot')
plt.xlabel('Study Hours')
plt.ylabel('Skill Development Hours')

plt.show()