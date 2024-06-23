import pandas as pd
values = [150, 250, 350, 450, 550, 650]
multi_index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)])
multi_series = pd.Series(values, index=multi_index)
print("Multi-index Series:")
print(multi_series)
subset_A = multi_series.loc['A']
print("\nSubset A:")
print(subset_A)
subset_A_2 = multi_series.loc[('A', 2)]
print("\nSubset A, Inner 2:")
print(subset_A_2)
subset_B = multi_series.loc['B']
print("\nSubset B:")
print(subset_B)
subset_C_1 = multi_series.loc[('C', 1)]
print("\nSubset C, Inner 1:")
print(subset_C_1)
subset_B_xs = multi_series.xs('B')
print("\nSubset B using xs:")
print(subset_B_xs)
subset_level_2 = multi_series.xs(2, level=1)
print("\nSubset Inner Level 2 using xs:")
print(subset_level_2)
