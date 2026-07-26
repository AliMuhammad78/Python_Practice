import os

# Set the directory path you want to list
# Use "." for the current directory, or specify an absolute/relative path
directory = "/"

try:
    contents = os.listdir(directory)
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"Error: Directory '{directory}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory}'.")
