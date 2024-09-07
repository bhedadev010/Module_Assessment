#3. Using NumPy, create a Pandas Data Frame with five rows and three columns.

import pandas as pd
import numpy as np

np_data = np.random.rand(5, 3)

df = pd.DataFrame(np_data, columns=['Column1', 'Column2', 'Column3'])

print(df)