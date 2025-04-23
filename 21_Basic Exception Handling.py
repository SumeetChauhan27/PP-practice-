print("Division Program with Exception Handling")

try:
    # Taking input from the user
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    
    # Performing division
    result = num1 / num2
    
    # Displaying result
    print(f"The result of {num1} ÷ {num2} is: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numeric values only.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
