import pandas as pd
import numpy as np

data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', np.nan, np.nan, np.nan],
    'Salary': [100, 200, np.nan, np.nan]
}

df = pd.DataFrame(data)

print("First 2 rows:")
print(df.head(2))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nTotal number of null values:")
print(df.isnull().sum())

print("\nDetailed info:")
print(df.info())

df_no_null_rows = df.dropna()
print("\nDataFrame with null rows dropped:")
print(df_no_null_rows)

df_no_null_cols = df.dropna(axis=1)
print("\nDataFrame with null columns dropped:")
print(df_no_null_cols)

df['Salary'].fillna(300, inplace=True)
print("\nAfter filling nulls in Salary with 300:")
print(df)

df['Role'].fillna('CEO', inplace=True)
print("\nAfter filling nulls in Role with 'CEO':")
print(df)

