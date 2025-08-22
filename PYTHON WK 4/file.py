def create_input_file():
    """Create sample input.txt file"""
    sample_content = [
        "Hello, this is a sample text file.",
        "It contains multiple lines of text for processing.",
        "We will count words and convert to uppercase.",
        "Python file handling is very useful for data processing.",
        "This is the fifth and final line of our input file."
    ]
    
    with open('input.txt', 'w') as file:
        for line in sample_content:
            file.write(line + '\n')
    
    print("input.txt created with sample content")

def process_files():
    """Main processing function"""
    import os
    
    # Create input file if it doesn't exist
    if not os.path.exists('input.txt'):
        create_input_file()
    
    try:
        # Read and process input file
        with open('input.txt', 'r') as input_file:
            original_content = input_file.read()
        
        # Count words
        words = original_content.split()
        word_count = len(words)
        
        # Convert to uppercase
        uppercase_content = original_content.upper()
        
        # Prepare output
        output_content = f"PROCESSED FILE CONTENT:\n{uppercase_content}\n"
        output_content += f"WORD COUNT: {word_count}\n"
        output_content += f"LINES: {original_content.count(chr(10)) + 1}\n"
        output_content += f"CHARACTERS: {len(original_content)}"
        
        # Write output
        with open('output.txt', 'w') as output_file:
            output_file.write(output_content)
        
        # Success message
        print("SUCCESS: output.txt created successfully!")
        print(f" Processed {word_count} words from input.txt")
        
        # Show preview
        print("Output preview:")
        print("-" * 30)
        lines = output_content.split('\n')
        for line in lines[:6]:  # Show first 6 lines
            print(line)
        if len(lines) > 6:
            print("... (truncated)")
        
    except Exception as e:
        print(f"Error: {e}")

# Run the script
if __name__ == "__main__":
    print("Processing files...")
    process_files()
    