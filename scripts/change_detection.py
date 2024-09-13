import joblib
import numpy as np

def apply_random_forest(before_img, after_img):
    # Load the trained model
    clf = joblib.load('model/random_forest_model.pkl')

    # Flatten the two-channel images (VV and VH) and concatenate them
    features_before = before_img.reshape(-1, 2)  # Flatten VV and VH channels for before image
    features_after = after_img.reshape(-1, 2)    # Flatten VV and VH channels for after image

    # Stack the before and after features to form the input for the model
    features = np.hstack([features_before, features_after])

    # Predict change map
    change_map = clf.predict(features)
    
    # Reshape the result back to image dimensions
    return change_map.reshape(before_img.shape[:2])
