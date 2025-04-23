def rupees_to_dollar():
    rupees = float(input("Enter amount in Rupees: ₹"))
    dollar = rupees / 83.0  # Example conversion rate
    print(f"Equivalent in Dollars: ${dollar:.2f}")

def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

def inches_to_feet():
    inches = float(input("Enter length in Inches: "))
    feet = inches / 12
    print(f"Length in Feet: {feet:.2f} ft")

def main():
    print("Choose a conversion option:")
    print("1. Rupees to Dollar")
    print("2. Celsius to Fahrenheit")
    print("3. Inches to Feet")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        rupees_to_dollar()
    elif choice == '2':
        celsius_to_fahrenheit()
    elif choice == '3':
        inches_to_feet()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

main()
