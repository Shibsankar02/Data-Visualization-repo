import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("student_data.csv")

scholarship = df['Do you have meritorious scholarship ?'].value_counts()

scholarship.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Scholarship Distribution')
plt.ylabel('')
plt.show()