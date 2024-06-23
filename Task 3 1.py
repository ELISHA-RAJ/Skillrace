import pandas as pd
import numpy as np

dates_data = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

values_data = np.random.randn(len(dates_data))

df_series = pd.DataFrame(values_data, index=dates_data, columns=['Measure'])

print(df_series.head())
