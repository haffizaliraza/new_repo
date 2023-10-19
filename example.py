import os
import random
import string

# Define the folder path where Python files are located
folder_path = './'

# Define the number of lines of random Python code to generate
num_lines = 10

# Function to generate random Python code
def generate_random_code():
    return 'Hi there'

# Loop through all Python files in the folder and write random code
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, 'a') as f:
                random_code = generate_random_code()
                f.write(random_code)
                print(f"Random code written to {file_path}")  
Hi there