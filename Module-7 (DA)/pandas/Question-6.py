#6. Write the code to show the number of rows and columns in data frame.

import pandas as pd

df = pd.read_csv('ipl-matches.csv')

num_rows, num_columns = df.shape

print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")