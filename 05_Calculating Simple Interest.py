def calculate_simple_interest():
    # Input from the user
    principal = float(input("Enter the Principal amount (₹): "))
    rate = float(input("Enter the Rate of Interest (% per annum): "))
    time = float(input("Enter the Time period (in years): "))

    # Calculate Simple Interest
    simple_interest = (principal * rate * time) / 100

    # Display the result
    print(f"\nSimple Interest = ₹{simple_interest:.2f}")

calculate_simple_interest()
