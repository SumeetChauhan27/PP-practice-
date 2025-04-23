# Function to read city names from a file, sort them, and write to another file

def sort_city_names(input_file, output_file): #city.txt
    # Open the input file in read mode
    infile = open(input_file, 'r')
    cities = [line.strip() for line in infile.readlines()]
    infile.close()  # Close the input file after reading

    # Sort the city names alphabetically
    cities.sort()

    # Open the output file in write mode
    outfile = open(output_file, 'w')
    for city in cities:
        outfile.write(city + '\n')
    outfile.close()  # Close the output file after writing

    print(f"City names have been sorted and written to '{output_file}'.")

# Main program
input_file = input("Enter the name of the input file (with city names): ")
output_file = input("Enter the name of the output file to store sorted cities: ")

# Call the function to sort city names and write to the output file
sort_city_names(input_file, output_file)
