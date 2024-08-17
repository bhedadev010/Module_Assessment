#1 Convert a 1D array to a 2D array with 2 rows

import numpy as np

array_1d = np.array([1, 2, 3, 4, 5, 6])

array_2d = array_1d.reshape(2, 3)

print(array_2d)