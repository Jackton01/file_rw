# File Read & Write with Error Handling

# Ask user for the input file
input_file = input("Enter the name of the file to read: ")

try:
    # Try opening the file in read mode
    with open(input_file, 'r') as file:
        content = file.read()

    # Example modification: convert all text to uppercase
    modified_content = content.upper()

    # Define output file name
    output_file = "modified_" + input_file

    # Write the modified content to the new file
    with open(output_file, 'w') as file:
        file.write(modified_content)

    print(f"File has been modified and saved as '{output_file}'")

# Handle errors if the file doesn't exist or can't be read
except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except IOError:
    print(f"Error: The file '{input_file}' could not be read or written.")
