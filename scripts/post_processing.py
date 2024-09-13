import cv2
import numpy as np

def clean_change_map(change_map):
    # Step 1: Remove small noise using morphological opening
    kernel = np.ones((3, 3), np.uint8)
    cleaned_map = cv2.morphologyEx(change_map, cv2.MORPH_OPEN, kernel)

    # Step 2: Fill small holes using morphological closing
    cleaned_map = cv2.morphologyEx(cleaned_map, cv2.MORPH_CLOSE, kernel)

    # Step 3: Optional - apply a median filter to smooth the image
    cleaned_map = cv2.medianBlur(cleaned_map, 5)

    # Step 4: Threshold the cleaned map (optional)
    _, cleaned_map = cv2.threshold(cleaned_map, 0, 255, cv2.THRESH_BINARY)

    return cleaned_map
