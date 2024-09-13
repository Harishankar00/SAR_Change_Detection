import cv2
import os

def apply_speckle_filter(image):
    if image is None:
        print("Error: Empty image passed to apply_speckle_filter.")
        return None
    return cv2.medianBlur(image, 5)

def load_images(before_vv_path, before_vh_path, after_vv_path, after_vh_path):
    # Load VV and VH images for before and after datasets
    before_vv = cv2.imread(before_vv_path, cv2.IMREAD_GRAYSCALE)
    before_vh = cv2.imread(before_vh_path, cv2.IMREAD_GRAYSCALE)
    after_vv = cv2.imread(after_vv_path, cv2.IMREAD_GRAYSCALE)
    after_vh = cv2.imread(after_vh_path, cv2.IMREAD_GRAYSCALE)

    # Check if images were loaded successfully
    if before_vv is None:
        print(f"Error: Could not load before VV image from {before_vv_path}")
    if before_vh is None:
        print(f"Error: Could not load before VH image from {before_vh_path}")
    if after_vv is None:
        print(f"Error: Could not load after VV image from {after_vv_path}")
    if after_vh is None:
        print(f"Error: Could not load after VH image from {after_vh_path}")

    # Only apply speckle filter if the image is successfully loaded
    if before_vv is not None:
        before_vv = apply_speckle_filter(before_vv)
    if before_vh is not None:
        before_vh = apply_speckle_filter(before_vh)
    if after_vv is not None:
        after_vv = apply_speckle_filter(after_vv)
    if after_vh is not None:
        after_vh = apply_speckle_filter(after_vh)

    return before_vv, before_vh, after_vv, after_vh

# Main
before_vv_path = 'D:/SAR_Change_Detection/data/before/before_vv/image_before_vv.tif'
before_vh_path = 'D:/SAR_Change_Detection/data/before/before_vh/image_before_vh.tif'
after_vv_path = 'D:/SAR_Change_Detection/data/after/after_vv/image_after_vv.tif'
after_vh_path = 'D:/SAR_Change_Detection/data/after/after_vh/image_after_vh.tif'

# Correct function call with the right variable names
before_vv_img, before_vh_img, after_vv_img, 
= load_images(before_vv_path, before_vh_path, after_vv_path, after_vh_path)

if before_vv_img is None or before_vh_img is None or after_vv_img is None or after_vh_img is None:
    print("Error: One or more images could not be processed. Please check the file paths and image data.")
else:
    print("Images loaded and processed successfully.")
