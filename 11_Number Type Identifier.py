# Program to identify if a number is even or odd

while True:
    try:
        # Taking user input
        num = int(input("Enter a number to check if it's even or odd: "))
        
        # Checking if the number is even or odd
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")
        
        # Exit loop after the check
        break
    
    except ValueError:
        # Handling invalid input (non-numeric input)
        print("Invalid input! Please enter a valid integer.")
