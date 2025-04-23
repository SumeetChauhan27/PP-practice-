# Program to generate multiplication table

# Taking user input for the number
num = int(input("Enter a number to generate its multiplication table: "))

# Generating multiplication table using a loop
print(f"Multiplication Table for {num}:")

# Looping through numbers 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
