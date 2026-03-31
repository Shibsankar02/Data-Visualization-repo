import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_data.csv")
df.columns = df.columns.str.strip()

# Use real data from dataset
x = df['How many hour do you study daily?'].values

# Create negative correlation from dataset
y = -x + np.random.normal(0, 0.3, len(x))

# Add an outlier
x = np.append(x, 0.5)
y = np.append(y, 6)

# Scatter plot
plt.scatter(x, y)

# Better title
plt.title('Inverse Relationship Between Study Time and Skill Activity')

plt.xlabel('Study Hours')
plt.ylabel('Derived Skill Activity')

plt.show()