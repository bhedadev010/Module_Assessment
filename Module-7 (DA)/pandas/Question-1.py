#1. Compute the minimum, 25th percentile, median, 75th, and maximum of ser.

import pandas as pd

ser = pd.Series([5, 3, 8, 6, 7, 2, 4, 9, 1])

minv = ser.min()
p_25 = ser.quantile(0.25)
mv = ser.median()
p_75 = ser.quantile(0.75)
maxv = ser.max()

print(f"Minimum: {minv}")
print(f"25th Percentile: {p_25}")
print(f"Median: {mv}")
print(f"75th Percentile: {p_75}")
print(f"Maximum: {maxv}")

