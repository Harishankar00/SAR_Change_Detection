from scripts.pre_processing import load_images
from scripts.feature_extraction import extract_features
from scripts.change_detection import apply_random_forest
from scripts.post_processing import clean_change_map
import cv2

# Define the paths for VV and VH images
before_vv_img = 'D:/SAR_Change_Detection/data/before/before_vv/image_before_vv.tif'
before_vh_img = 'D:/SAR_Change_Detection/data/before/before_vh/image_before_vh.tif'
after_vv_img = 'D:/SAR_Change_Detection/data/after/after_vv/image_after_vv.tif'
after_vh_img = 'D:/SAR_Change_Detection/data/after/after_vh/image_after_vh.tif'

# Load before and after images (VV and VH)
before_img, after_img = load_images(before_vv_img, before_vh_img, after_vv_img, after_vh_img)

# Extract features for both VV and VH
features_before = extract_features(before_img)
features_after = extract_features(after_img)

# Detect changes using Random Forest
change_map = apply_random_forest(features_before, features_after)

# Clean up the change map (optional post-processing)
cleaned_map = clean_change_map(change_map)

# Save the results
cv2.imwrite('results/change_map.tif', cleaned_map)
