import zipfile
import os

# Paths of the files and folder you want to zip
png_file = 'pack.png'
mcmeta_file = 'pack.mcmeta'
folder_to_zip = 'assets'

# Name of the output zip file
output_zip_filename = 'pack.zip'

# Count the total number of files to estimate progress
total_files = sum(len(files) for _, _, files in os.walk(folder_to_zip)) + 2  # Add 2 for the individual files

try:
    os.remove(output_zip_filename)
    print(f"File '{output_zip_filename}' deleted successfully.")
except OSError as e:
    print(f"Error deleting '{output_zip_filename}': {e}")



# Create a new zip file
with zipfile.ZipFile(output_zip_filename, 'w') as zipf:
    print("Zipping files...")
    # Add the individual files to the zip archive
    zipf.write(png_file)
    zipf.write(mcmeta_file)

    # Recursively add all files and subdirectories in the folder to the zip archive
    progress = 0
    for folder_root, _, files in os.walk(folder_to_zip):
        for file in files:
            file_path = os.path.join(folder_root, file)
            arcname = os.path.join('assets', os.path.relpath(file_path, folder_to_zip))
            zipf.write(file_path, arcname=arcname)
            progress += 1
            print(f"Progress: {progress}/{total_files}", end='\r')  # Print progress inline
    print(f"Progress: {total_files}/{total_files}")

print(f"Successfully created {output_zip_filename}")

