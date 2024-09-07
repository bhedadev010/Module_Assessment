#7. How might you show the first few rows of data frame?

import pandas as pd

df = pd.read_csv('ipl-matches.csv')

print(df.head())
