"""
Program to create a random NumPy array, sort it and reshape it into a matrix.
"""

import numpy as np

# create array
array = np.random.randint(1, 100, 12) # 12 random number from 1 to 99 
print("Original array")
print(array)

# sort the array
sorted_array = np.sort(array)
print("Sorted array")
print(sorted_array)

# reshape array
reshaped_arr = sorted_array.reshape(3, 4) # reshape into 3x4
print("Reshaped array of 3x4 is")
print(reshaped_arr)


