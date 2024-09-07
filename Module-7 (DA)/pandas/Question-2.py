#2. Creating A Pandas Data Frame and Using Sample Data Sets

import numpy as np
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print(df)

print(df.head())
print(df.tail())
print(df.sample())