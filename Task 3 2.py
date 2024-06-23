import pandas as pd

start_date_first = '2024-01-01'
end_date_first = '2024-12-31'
date_index_first = pd.date_range(start=start_date_first, end=end_date_first)
print(date_index_first)

start_date_second = '2024-01-01'
periods_second = 365  # for a full year
date_index_second = pd.date_range(start=start_date_second, periods=periods_second)
print(date_index_second)

end_date_third = '2024-12-31'
periods_third = 365  # for a full year
date_index_third = pd.date_range(end=end_date_third, periods=periods_third)
print(date_index_third)

start_date_fourth = '2024-01-01'
end_date_fourth = '2024-12-31'
date_index_fourth = pd.date_range(start=start_date_fourth, end=end_date_fourth, freq='D')
print(date_index_fourth)
