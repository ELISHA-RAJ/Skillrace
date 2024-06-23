import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)

data_dict = {
    'Group': np.random.choice(['G1', 'G2', 'G3', 'G4', 'G5'], 100),
    'Values': np.random.randn(100)
}

df_data = pd.DataFrame(data_dict)

plt.figure(figsize=(12, 6))
sns.boxplot(x='Group', y='Values', data=df_data)
plt.xlabel('Group')
plt.ylabel('Values')
plt.title('Box Plot of Values by Group')
plt.grid(True)
plt.show()
