import os
import shutil

# Define the source directory (where all images are stored)
source_directory = r'C:\Users\dhanv\Downloads\archive (4)\KAGGLE-2018'  # Use raw string for Windows paths

# Define the destination directories for VV and VH images
vh_directory = r'D:\SAR_Change_Detection\data\image_before_pre\dataset_sar_vh'
vv_directory = r'D:\SAR_Change_Detection\data\image_before_pre\dataset_sar_vv'

# Create destination directories if they don't exist
if not os.path.exists(vh_directory):
    os.makedirs(vh_directory)

if not os.path.exists(vv_directory):
    os.makedirs(vv_directory)

# Loop through all files in the source directory
for root, dirs, files in os.walk(source_directory):
    for file in files:
        # Check if the file name starts with 's1a-iw-grd-vh' or 's1a-iw-grd-vv'
        if file.lower().startswith('s1a-iw-grd-vh'):
            # Move the file to the VH directory
            file_path = os.path.join(root, file)
            shutil.move(file_path, os.path.join(vh_directory, file))
            print(f"Moved VH file: {file}")
        
        elif file.lower().startswith('s1a-iw-grd-vv'):
            # Move the file to the VV directory
            file_path = os.path.join(root, file)
            shutil.move(file_path, os.path.join(vv_directory, file))
            print(f"Moved VV file: {file}")

print("Separation of SAR images completed.")
