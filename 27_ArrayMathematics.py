import numpy as np

# Create two arrays of the same shape
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print("Array A:", a)
print("Array B:", b)

# Element-wise operations
print("\nElement-wise Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Dot product
dot_product = np.dot(a, b)
print("\nDot Product:", dot_product)

# Cross product
cross_product = np.cross(a, b)
print("Cross Product:", cross_product)
