import os

def collect_python_files(start_path):
    python_files = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith('.py'):
                # Get relative path from start_path
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, start_path)
                python_files.append(rel_path)
    return python_files

if __name__ == "__main__":
    # Get all Python files in src/flock
    flock_path = "src/flock"
    python_files = collect_python_files(flock_path)
    
    # Write to output file
    with open("flock_python_files.txt", "w") as f:
        for file_path in sorted(python_files):
            f.write(f"{file_path}\n")
    
    print(f"Found {len(python_files)} Python files. Paths written to flock_python_files.txt")
