# import os
# import sys
# from plantuml import PlantUML

# # Define the PlantUML server
# plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')

# # Function to create the png directory if it doesn't exist
# def create_png_directory():
#     if not os.path.exists('png'):
#         os.makedirs('png')
#         print("Created 'png' directory.")
#     else:
#         print("'png' directory already exists.")

# # Function to generate diagram from a .txt file
# def generate_diagram_from_txt(file_name):
#     # Extract title from file name
#     title = os.path.splitext(file_name)[0]
    
#     # Specify the output PNG path
#     output_file = os.path.join('png', f"{title}.png")

#     # Generate the PNG file using PlantUML
#     try:
#         plantuml.processes_file(file_name, outfile=output_file)
#         print(f"Generated diagram: {output_file}")
#     except Exception as e:
#         print(f"Error generating diagram: {e}")

# # Function to handle all .txt files or a specific one
# def process_files(file_name=None):
#     if file_name == 'all':
#         # Process all .txt files in the current directory
#         txt_files = [f for f in os.listdir() if f.endswith('.txt')]
#         if not txt_files:
#             print("No .txt files found in the current directory.")
#         for txt_file in txt_files:
#             generate_diagram_from_txt(txt_file)
#     else:
#         # Process a single specified .txt file
#         if not file_name.endswith('.txt'):
#             print(f"{file_name} is not a valid .txt file")
#             return
#         if not os.path.exists(file_name):
#             print(f"{file_name} not found.")
#             return
#         generate_diagram_from_txt(file_name)

# if __name__ == '__main__':
#     # Ensure the correct number of arguments are provided
#     if len(sys.argv) != 2:
#         print("Usage: python diagramming.py <filename>.txt or 'all'")
#     else:
#         file_name = sys.argv[1]
#         # Create the png directory
#         create_png_directory()
#         # Process the specified files
#         process_files(file_name)


import os
import sys
from plantuml import PlantUML

# Define the PlantUML server
plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')

# Function to create the png directory in a given folder
def create_png_directory(directory):
    png_dir = os.path.join(directory, 'png')
    if not os.path.exists(png_dir):
        os.makedirs(png_dir)
        print(f"Created 'png' directory in {directory}.")
    else:
        print(f"'png' directory already exists in {directory}.")
    return png_dir

# Function to generate diagram from a .txt file in the specified directory
def generate_diagram_from_txt(directory, file_name):
    # Extract title from file name
    title = os.path.splitext(file_name)[0]
    
    # Specify the output PNG path
    output_file = os.path.join(directory, 'png', f"{title}.png")

    # Generate the PNG file using PlantUML
    try:
        plantuml.processes_file(os.path.join(directory, file_name), outfile=output_file)
        print(f"Generated diagram: {output_file}")
    except Exception as e:
        print(f"Error generating diagram for {file_name}: {e}")

# Function to handle .txt files in a specific directory
def process_files_in_directory(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' not found.")
        return
    
    # Create the png directory within the specified directory
    png_dir = create_png_directory(directory)
    
    # Get all .txt files in the directory
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    if not txt_files:
        print(f"No .txt files found in directory: {directory}.")
        return
    
    # Process each .txt file in the directory
    for txt_file in txt_files:
        generate_diagram_from_txt(directory, txt_file)

# Function to handle a specific .txt file
def process_single_file(file_path):
    # Ensure the file exists
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return
    
    # Extract the directory and filename
    directory, file_name = os.path.split(file_path)
    
    # If no directory is specified, use the current directory
    if directory == '':
        directory = '.'
    
    # Create png directory in the specified directory
    png_dir = create_png_directory(directory)
    
    # Generate the diagram from the specific file
    generate_diagram_from_txt(directory, file_name)

# Main function to handle input arguments
def main():
    if len(sys.argv) != 2:
        print("Usage: python diagramming.py <directory> or <filename>.txt")
        return
    
    argument = sys.argv[1]

    # If argument is a directory, process all .txt files in the directory
    if os.path.isdir(argument):
        process_files_in_directory(argument)
    # If argument is a .txt file, process only that file
    elif argument.endswith('.txt'):
        process_single_file(argument)
    else:
        print(f"'{argument}' is not a valid directory or .txt file.")

if __name__ == '__main__':
    main()

