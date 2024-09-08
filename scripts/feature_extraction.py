import cv2
import numpy as np

def extract_features(image):
    # Edge detection (Canny)
    edges = cv2.Canny(image, 100, 200)
    
    # Texture features (using Laplacian filter)
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    
    return np.dstack((edges, laplacian))

def prepare_feature_set(before_img, after_img):
    # Extract features from both images
    before_features = extract_features(before_img)
    after_features = extract_features(after_img)
    
    # Calculate the difference in features between before and after images
    feature_diff = np.abs(after_features - before_features)
    
    return feature_diff.reshape(-1, feature_diff.shape[-1])  # Flatten for Random Forest input
