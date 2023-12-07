import os
import shutil
import glob
# Copy a file
shutil.copy('source_file.txt', 'destination_folder')

# Rename a file
os.rename('old_name.txt', 'new_name.txt')

# Delete a file
os.remove('file_to_delete.txt')

# Create a directory
os.mkdir('new_directory')

# List files in a directory
files = os.listdir('directory_path')
for file in files:
print(file)

# Get files matching a pattern
matched_files = glob.glob('*.txt')
print(matched_files)
