import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv('company_dataset.csv')
df_20 = df.head(20).copy()

df_20['ratings'] = pd.to_numeric(df_20['ratings'], errors='coerce')

def clean_reviews(x):
    x = str(x)
    x = re.sub(r'[^0-9.]', '', x)
    return float(x) if x else None

df_20['review_count'] = df_20['review_count'].apply(clean_reviews)
df_20['employee_count'] = df_20['employees'].str.extract(r'(\d+)').astype(float)

# Funnel (Barh)
df_20.sort_values(by='review_count', ascending=False)\
    .plot.barh(x='name', y='review_count')
plt.gca().invert_yaxis()
plt.show()