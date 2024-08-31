import os
import shutil

# Define the source and destination directories
source_folder = '/home/akil/Downloads'  # Replace with the path to your source folder
destination_folder = '/home/akil/Music/MP3'  # Replace with the path to your destination folder

# Ensure the destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List all files in the source directory
for filename in os.listdir(source_folder):
    # Check if the file has a .mp3 extension
    if filename.endswith('.mp3'):
        # Construct full file path
        file_path = os.path.join(source_folder, filename)
        # Move the file to the destination directory
        shutil.move(file_path, destination_folder)

print('MP3 files have been moved successfully.')

