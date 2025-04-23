# Function to extract words of a specified length from a text file

def extract_words_by_length(file_name, word_length): #file : test.txt
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the content of the file
            text = file.read()
            
            # Split the text into words using space and newline as delimiters
            words = text.split()
            
            # Filter words that have the specified length
            filtered_words = [word for word in words if len(word) == word_length]
            
            # Print the filtered words
            if filtered_words:
                print(f"Words of length {word_length}:")
                for word in filtered_words:
                    print(word)
            else:
                print(f"No words of length {word_length} found.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
file_name = input("Enter the name of the text file (with extension): ")
word_length = int(input("Enter the word length to search for: "))

# Call the function to extract words of the specified length
extract_words_by_length(file_name, word_length)
