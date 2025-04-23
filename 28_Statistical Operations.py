import numpy as np

# Sample data array
data = np.array([10, 20, 30, 40, 50, 60])

print("Data:", data)

# Mean
mean = np.mean(data)
print("Mean:", mean)

# Median
median = np.median(data)
print("Median:", median)

# Standard Deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Variance
variance = np.var(data)
print("Variance:", variance)

# Correlation Coefficient (with another sample array)
data2 = np.array([5, 15, 25, 35, 45, 55])
correlation_matrix = np.corrcoef(data, data2)

print("\nSecond Data Set:", data2)
print("Correlation Coefficient Matrix:\n", correlation_matrix)
print("Correlation Coefficient between data and data2:", correlation_matrix[0, 1])
