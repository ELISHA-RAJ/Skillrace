import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x_data = np.random.rand(100)
y_data = 2 * x_data + np.random.normal(0, 0.1, 100)

plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, alpha=0.7)
plt.xlabel('X Data')
plt.ylabel('Y Data')
plt.title('Scatter Plot of X Data vs. Y Data')
plt.grid(True)
plt.show()
