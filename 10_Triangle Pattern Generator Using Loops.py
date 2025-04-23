
# Define the height of the triangle
height = int(input("Enter the height of the triangle: "))

# Loop for each row
for i in range(1, height + 1):
    # Printing spaces before the stars
    for j in range(height - i):
        print(" ", end="")  # This prints space without a newline

    # Loop to print the stars
    for k in range(1, i + 1):
        print("*", end="")  # This prints the star without a newline

    # Move to the next line after each row
    print()
