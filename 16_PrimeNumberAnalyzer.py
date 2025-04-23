# Function to check if a number is prime
def is_prime(num):
    # Handle edge cases for numbers less than 2
    if num <= 1:
        return False
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # num is divisible by i, so it's not prime
    return True  # num is prime

# Taking user input
number = int(input("Enter a number to check if it is prime: "))

# Calling the function and displaying the result
if is_prime(number):
    print(f"{number} is a Prime number.")
else:
    print(f"{number} is not a Prime number.")
