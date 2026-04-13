"""
Program to generate a NumPy array and perform sum, mean, max and min operations.
"""

import numpy as np

a = np.array([1, 10 ,50, 100 ,130 , 12430]) # 1d array of 6 elements
print("The 1d array is: ", a)

sum = np.sum(a) # sum of all elements in the array
print("The sum of the array is: ", sum)

mean = np.mean(a) # mean of the array
print("The mean of the array is: ", mean)

largest = np.max(a) # largest element in the array
print("The largest element in the array is: ", largest)

smallest = np.min(a) # smallest element in the array
print("The smallest element in the array is: ", smallest)