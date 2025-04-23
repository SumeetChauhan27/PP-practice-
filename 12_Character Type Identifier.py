# Program to check the character type

# Taking user input
char = input("Enter a character: ")

# Check if the input is a digit
if char.isdigit():
    print(f"'{char}' is a Digit.")
# Check if the input is a lowercase character
elif char.islower():
    print(f"'{char}' is a Lowercase Character.")
# Check if the input is an uppercase character
elif char.isupper():
    print(f"'{char}' is an Uppercase Character.")
# Check if the input is a special character
else:
    print(f"'{char}' is a Special Character.")
