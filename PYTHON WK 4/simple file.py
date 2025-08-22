# Simple File Copier
print(" Simple File Program")

# Ask for file names
input_file = input("Enter the file to read: ")
output_file = input("Enter the new file to create: ")

# Read and copy the file
try:
    # Read the original file
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Make it uppercase (simple modification)
    new_content = content.upper()
    
    # Write to new file
    with open(output_file, 'w') as file:
        file.write(new_content)
    
    print(f"Done! Created '{output_file}'")
    
except FileNotFoundError:
    print(f"Error: '{input_file}' not found!")
except:
    print("Something went wrong!")