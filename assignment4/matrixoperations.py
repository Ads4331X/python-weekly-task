"""
Program to perform matrix addition, subtraction and multiplication using NumPy with validation.
"""

import numpy as np

def input_matrix(name):
    # ask user for rows and cols of the matrix
    rows = int(input(f'Enter the row of {name}: ')) 
    cols = int(input(f'Enter the col of {name}: '))

    print(f'Enter the elements of {name}') 
    elements = []

    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f'Enter element at row {i}, column {j}: '))
            row.append(value)
        elements.append(row)

    return np.array(elements) 

try:
    A = input_matrix("A") # passing name = A
    B = input_matrix("B") # passing name = B

    print("Matrix A:")
    print(A)
    print()
    print("Matrix B:")
    print(B)
    print()

    if A.shape == B.shape:
        print("Addition of matrix A and B is:")
        print(A + B)
        print()
        print("Subtraction of matrix A and B is:")
        print(A - B)
        print()
    else:
        print("\nError: Addition and Subtraction not possible: Matrices must have the same dimensions.")

    if A.shape[1] == B.shape[0]:
        print("Multiplication of matrix A and B is:")
        print(np.dot(A, B))
    else:
        print("\nError: Multiplication not possible: Columns of A must equal rows of B.")

except ValueError as e:
    print("\nError:", e)








