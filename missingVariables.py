import pandas as pd
import numpy as np

data={
    "Name":["A","B","C","D"],
    "Age":[20,np.nan,22,None],
    "Salary":[20000,25000,None,30000]
}

df=pd.DataFrame(data)
print(df)