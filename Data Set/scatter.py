import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("student_data.csv")

plt.scatter(
    df['How many hour do you study daily?'],
    df['What is your current CGPA?'],
    color='green'
)

plt.title('Study Hours vs CGPA')
plt.xlabel('Study Hours')
plt.ylabel('CGPA')
plt.show()