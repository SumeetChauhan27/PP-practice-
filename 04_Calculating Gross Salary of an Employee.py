def calculate_gross_salary():
    # Input basic salary
    basic_salary = float(input("Enter the Basic Salary (₹): "))

    # Calculate allowances
    da = 0.70 * basic_salary  # Dearness Allowance
    ta = 0.30 * basic_salary  # Travel Allowance
    hra = 0.10 * basic_salary  # House Rent Allowance

    # Calculate gross salary
    gross_salary = basic_salary + da + ta + hra

    # Display result
    print("\n--- Salary Breakdown ---")
    print(f"Basic Salary      : ₹{basic_salary:.2f}")
    print(f"Dearness Allowance: ₹{da:.2f}")
    print(f"Travel Allowance  : ₹{ta:.2f}")
    print(f"House Rent Allow. : ₹{hra:.2f}")
    print(f"-----------------------------")
    print(f"Gross Salary      : ₹{gross_salary:.2f}")

calculate_gross_salary()
