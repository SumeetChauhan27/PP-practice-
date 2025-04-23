# Program to generate Fibonacci sequence using a while loop

# Taking user input for number of terms
n = int(input("Enter the number of terms for Fibonacci sequence: "))

# Initializing the first two terms of the Fibonacci sequence
a, b = 0, 1
count = 0

print("Fibonacci Sequence:")

# Using a while loop to generate Fibonacci sequence
while count < n:
    print(a, end=" ")
    # Update the values of a and b for the next term
    a, b = b, a + b
    count += 1
