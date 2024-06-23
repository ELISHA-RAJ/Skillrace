import pandas as pd

start_date_utc = '2024-01-01'
end_date_utc = '2024-01-05'
date_index_utc = pd.date_range(start=start_date_utc, end=end_date_utc, freq='D', tz='UTC')
print(date_index_utc)

date_index_ny = pd.date_range(start=start_date_utc, end=end_date_utc, freq='D')
date_index_ny = date_index_ny.tz_localize('America/New_York')
print(date_index_ny)

date_index_london = date_index_ny.tz_convert('Europe/London')
print(date_index_london)

date_index_utc_3days = pd.date_range(start=start_date_utc, periods=3, freq='D', tz='UTC')
date_index_ny_3days = pd.date_range(start=start_date_utc, periods=3, freq='D', tz='America/New_York')
combined_index = date_index_utc_3days.union(date_index_ny_3days)
print(combined_index)

