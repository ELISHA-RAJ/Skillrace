import pandas as pd

# Define a starting period
period_start = pd.Period('2024-01', freq='M')

# Calculate future and past periods
future_period = period_start + 3
print("Future Period:", future_period)

past_period = period_start - 2
print("Past Period:", past_period)

# Construct a range of periods from January to December 2024
periods_range = pd.period_range(start='2024-01', end='2024-12', freq='M')
print("Periods Range:", periods_range)
