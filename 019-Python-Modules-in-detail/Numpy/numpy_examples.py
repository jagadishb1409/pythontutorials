import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# Mathematical Functions and Operations

arr = np.array([1, 2, 3])

# Square root
print(np.sqrt(arr))

# Exponential
print(np.exp(arr))

# Trigonometric functions
print(np.sin(arr))
print(np.cos(arr))

# Indexing and Slicing

arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0])    # Output: 1
print(arr[-1])   # Output: 5

# Slicing
print(arr[1:4])  # Output: [2 3

print(arr[:3])   # Output: [1 2 3]
print(arr[::2])  # Output: [1 3 5]

# Broadcasting

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])

# Broadcasting addition
result = arr1 + arr2

print(result)

# Linear Algebra Operations

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = np.dot(arr1, arr2)

print(result)