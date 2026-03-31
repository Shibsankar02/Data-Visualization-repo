import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("student_data.csv")

df_sorted = df.sort_values('How many Credit did you have completed?')

plt.step(
    df_sorted['How many Credit did you have completed?'],
    df_sorted['What is your current CGPA?'],
    where='mid'
)

plt.title('Credits vs CGPA (Step Chart)')
plt.xlabel('Credits')
plt.ylabel('CGPA')
plt.show()