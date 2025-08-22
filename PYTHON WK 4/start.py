import os

def process_file_with_error_handling(input_file_path, output_file_path):
    """
    Reads a file, modifies its content, and writes the modified content to a new file.
    Includes error handling for file-related issues.

    Args:
        input_file_path (str): The path to the file to be read.
        output_file_path (str): The path to the file to be written.
    """
    print("\n--- Starting file processing ---")
    
    modified_content = ""
    
    try:
        # Use a 'with' statement for safe file handling.
        # It automatically closes the file even if an error occurs.
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            original_content = input_file.read()
            print(f"Successfully read content from '{input_file_path}'.")
            
            # --- File Modification Logic ---
            # A simple modification: convert all text to uppercase.
            modified_content = original_content.upper()
            
            # You can add more complex modifications here, for example:
            # - Prepend a header: modified_content = "Modified by the program:\n" + modified_content
            # - Replace certain words: modified_content = modified_content.replace('old', 'new')
            
    except FileNotFoundError:
        print(f"ERROR: The file '{input_file_path}' was not found. Please check the filename and try again.")
        return False
    except IOError as e:
        print(f"ERROR: An I/O error occurred while reading '{input_file_path}'. Details: {e}")
        return False
    
    # If the reading was successful, proceed to write the new file.
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_content)
            print(f"Successfully wrote modified content to '{output_file_path}'.")
            return True
    except IOError as e:
        print(f"ERROR: An I/O error occurred while writing to '{output_file_path}'. Details: {e}")
        return False

# --- Main Program Execution ---
if __name__ == "__main__":
    print("Welcome to the File Processor!")
    print("This program will read a file, convert its text to uppercase, and save it to a new file.")
    
    while True:
        # Get filenames from the user.
        input_filename = input("\Enter the name of the file to read ('input.txt'): ").strip()
        output_filename = input("Enter the name for the new file ('output.txt'): ").strip()

        # Check if filenames are empty.
        if not input_filename or not output_filename:
            print("Filenames cannot be empty. Please provide valid names.")
            continue
            
        # Call the processing function.
        success = process_file_with_error_handling(input_filename, output_filename)
        
        # Ask the user if they want to run the program again.
        if success:
            retry = input("\Processing complete! Do you want to process another file? (yes/no): ").lower()
            if retry != 'yes':
                break
        else:
            retry = input("\File processing failed. Do you want to try again? (yes/no): ").lower()
            if retry != 'yes':
                break
                
    print("\Thank you for using the File Processor. Goodbye!")