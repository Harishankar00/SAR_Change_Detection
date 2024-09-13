import cv2
import numpy as np

def extract_features(image):
    # Split the two-channel image into VV and VH
    vv, vh = cv2.split(image)

    # Example: Use Sobel operator to extract edges for both VV and VH
    sobelx_vv = cv2.Sobel(vv, cv2.CV_64F, 1, 0, ksize=5)
    sobely_vv = cv2.Sobel(vv, cv2.CV_64F, 0, 1, ksize=5)
    
    sobelx_vh = cv2.Sobel(vh, cv2.CV_64F, 1, 0, ksize=5)
    sobely_vh = cv2.Sobel(vh, cv2.CV_64F, 0, 1, ksize=5)

    # Combine the features from VV and VH (you can customize this)
    features_vv = np.sqrt(sobelx_vv ** 2 + sobely_vv ** 2)
    features_vh = np.sqrt(sobelx_vh ** 2 + sobely_vh ** 2)

    # Return combined features as a 2-channel image
    return np.stack([features_vv, features_vh], axis=-1)
