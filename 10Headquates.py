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

# Top HQ

print("\nTop 10 Companies with Headquarters:\n")

top_10 = df_20[['name', 'hq']].head(10)

for index, row in top_10.iterrows():
    print(f"{row['name']}  -->  {row['hq']}")