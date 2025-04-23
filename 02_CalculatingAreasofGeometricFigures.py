import math

def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"Area of the circle: {area:.2f}")

def area_of_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"Area of the rectangle: {area:.2f}")

def area_of_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"Area of the triangle: {area:.2f}")

def main():
    print("Choose a geometric figure to calculate its area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        area_of_circle()
    elif choice == '2':
        area_of_rectangle()
    elif choice == '3':
        area_of_triangle()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# Run the program
main()

