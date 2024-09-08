from scripts.pre_processing import load_images
from scripts.change_detection import apply_random_forest
from scripts.post_processing import post_process_change_map, vectorize_change_map
import numpy as np

if __name__ == "__main__":
    # Load SAR images
    before_img, after_img = load_images('data/image_before.tif', 'data/image_after.tif')
    
    # Apply Random Forest to detect changes
    change_map = apply_random_forest(before_img, after_img)
    
    # Save raw change map
    np.save('results/change_map.npy', change_map)
    
    # Post-process the change map
    filtered_map = post_process_change_map(change_map)
    
    # Vectorize the results and save as GeoJSON
    vectorize_change_map(filtered_map)
