import cv2
import numpy as np

def apply_speckle_filter(image):
    # Apply a median filter for noise reduction (speckle noise in SAR images)
    return cv2.medianBlur(image, 5)

def load_images(before_path, after_path):
    # Load SAR images before and after
    before_img = cv2.imread(before_path, cv2.IMREAD_GRAYSCALE)
    after_img = cv2.imread(after_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply speckle filter
    before_img = apply_speckle_filter(before_img)
    after_img = apply_speckle_filter(after_img)
    
    return before_img, after_img
