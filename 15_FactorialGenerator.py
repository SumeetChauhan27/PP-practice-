# Program to compute the factorial of a given integer N

# Taking user input
N = int(input("Enter a number to compute its factorial: "))

# Initializing the factorial variable
factorial = 1

# Using a loop to calculate the factorial
if N < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, N + 1):
        factorial *= i  # Multiply the current value of factorial by i

    # Displaying the result
    print(f"The factorial of {N} is {factorial}")