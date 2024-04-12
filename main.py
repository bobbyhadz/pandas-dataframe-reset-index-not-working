# Pandas: DataFrame.reset_index() not working

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 3, 1, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
}, index=['A', 'B', 'C', 'D'])

print(df)

df = df.reset_index()

print('-' * 50)
print(df)