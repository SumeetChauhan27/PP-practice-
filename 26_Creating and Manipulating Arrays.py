import numpy as np

# 1D Array
print("1D Array:")
array_1d = np.array([10, 20, 30, 40, 50])
print("Original 1D array:", array_1d)

# Indexing
print("Element at index 2:", array_1d[2])

# Slicing
print("Slice from index 1 to 3:", array_1d[1:4])

# 2D Array
print("\n2D Array:")
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D array:\n", array_2d)

# Indexing
print("Element at (1, 2):", array_2d[1, 2])

# Slicing
print("First row:", array_2d[0, :])
print("Second column:", array_2d[:, 1])

# Reshaping
reshaped_2d = array_2d.reshape(3, 2)
print("Reshaped 2D array (3x2):\n", reshaped_2d)

# 3D Array
print("\n3D Array:")
array_3d = np.array([[[1, 2], [3, 4]],
                     [[5, 6], [7, 8]]])
print("Original 3D array:\n", array_3d)

# Indexing
print("Element at (1, 0, 1):", array_3d[1, 0, 1])

# Slicing
print("First 2D block:\n", array_3d[0])

# Reshaping
reshaped_3d = array_3d.reshape(4, 2)
print("Reshaped 3D array to 2D (4x2):\n", reshaped_3d)
