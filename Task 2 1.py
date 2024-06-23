import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = np.random.normal(loc=0, scale=1, size=1000)


plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(data, fill=True)
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Density Plot of Random Data')
plt.grid(True)
plt.show()
