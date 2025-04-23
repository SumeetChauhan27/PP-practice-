def basic_arithmetic_operations():
    # Input two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform arithmetic operations
    print("\n--- Results of Basic Arithmetic Operations ---")
    print(f"Addition:        {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction:     {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication:  {num1} * {num2} = {num1 * num2}")
    
    # Division and modulus should handle division by zero
    if num2 != 0:
        print(f"Division:        {num1} / {num2} = {num1 / num2}")
        print(f"Modulus:         {num1} % {num2} = {num1 % num2}")
    else:
        print("Division:        Undefined (cannot divide by zero)")
        print("Modulus:         Undefined (cannot divide by zero)")

basic_arithmetic_operations()

