# For a Pandas Data Frame created from a NumPy array, what is the default behavior for
# the labels for the columns? For the rows?

import pandas as pd
import numpy as np

np_data = np.random.rand(5, 3)
df = pd.DataFrame(np_data)

print(df)

#The default column labels are integers starting from 0 and incrementing by 1 for each column
#the default row labels (index) are integers starting from 0 and incrementing by 1 for each row.