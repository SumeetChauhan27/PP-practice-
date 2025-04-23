def calculate_area(radius):
    pi = 3.14
    return pi * radius ** 2

def calculate_circumference(radius):
    pi = 3.14
    return pi * radius * 2

def main():
    radius = 5
    import pdb; pdb.set_trace()  # Debugger breakpoint
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")

if __name__ == "__main__":
    main()
