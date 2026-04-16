"""
Program to generate a NumPy array and perform sum, mean, max and min operations.
"""

import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

# Sum
total_sum = np.sum(arr)
print("Total Sum:", total_sum)

# Mean
mean_value = np.mean(arr)
print("Mean:", mean_value)

# Max and Min
maximum = np.max(arr)
minimum = np.min(arr)

print("Maximum value:", maximum)
print("Minimum value:", minimum)