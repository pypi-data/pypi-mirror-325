import os


# Function to iterate over all Python files and collect their contents
def collect_python_files(folder_path, output_file):
    try:
        # Open the output file in write mode
        with open(output_file, "w", encoding="utf-8") as txt_file:
            # Walk through the folder and its subfolders
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if "flock\\app" in root:
                        continue
                    # Check if the file is a Python file
                    if file.endswith(".py"):
                        file_path = os.path.join(root, file)

                        # Read the content of the Python file
                        with open(file_path, encoding="utf-8") as py_file:
                            content = py_file.read()

                        # Write the content to the output file
                        txt_file.write(f"# File: {file_path}\n")
                        txt_file.write(content)
                        txt_file.write("\n\n")

        print(f"All Python files have been collected into {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    folder_path = input("Enter the folder path to search for Python files: ")
    output_file = input("Enter the name of the output text file (e.g., collected_files.txt): ")
    collect_python_files(folder_path, output_file)
