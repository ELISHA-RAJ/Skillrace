import pandas as pd
import numpy as np

data = {
    'P': [15, 25, np.nan, 45, 55, np.nan, 75],
    'Q': [np.nan, 25, 35, 45, np.nan, 65, 75],
    'R': ['red', 'blue', 'green', np.nan, 'yellow', 'orange', 'purple'],
    'S': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

missing_data = df.isna()
print("\nMissing Data in DataFrame:")
print(missing_data)

df_dropna_rows = df.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(df_dropna_rows)

df_dropna_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing data:")
print(df_dropna_cols)

df_fillna = df.fillna(value={'P': df['P'].mean(), 'Q': df['Q'].mean(), 'R': 'missing', 'S': 0})
print("\nDataFrame after filling missing data:")
print(df_fillna)

df_with_duplicates = df.append(df.iloc[2], ignore_index=True)
print("\nDataFrame with Duplicates:")
print(df_with_duplicates)

duplicates = df_with_duplicates.duplicated()
print("\nDuplicates in DataFrame:")
print(duplicates)

df_no_duplicates = df_with_duplicates.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)
