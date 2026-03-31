import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("student_data.csv")

df['Gender'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()