import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("student_data.csv")

df_sorted = df.sort_values('Average attendance on class')

plt.plot(
    df_sorted['Average attendance on class'],
    df_sorted['What is your current CGPA?'],
    marker='o'
)

plt.title('Attendance vs CGPA')
plt.xlabel('Attendance')
plt.ylabel('CGPA')
plt.show()