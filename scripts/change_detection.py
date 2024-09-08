import joblib
import numpy as np
from scripts.feature_extraction import prepare_feature_set
from scripts.pre_processing import load_images

def apply_random_forest(before_img, after_img):
    # Load the trained model
    clf = joblib.load('model/random_forest_model.pkl')
    
    # Extract features and compute feature differences
    features = prepare_feature_set(before_img, after_img)
    
    # Predict changes using the Random Forest
    change_map = clf.predict(features)
    
    return change_map.reshape(before_img.shape)  # Reshape to the original image size

if __name__ == "__main__":
    # Load SAR images
    before_img, after_img = load_images('data/image_before.tif', 'data/image_after.tif')
    
    # Apply the model to detect changes
    change_map = apply_random_forest(before_img, after_img)
    
    # Save the change map
    np.save('results/change_map.npy', change_map)
