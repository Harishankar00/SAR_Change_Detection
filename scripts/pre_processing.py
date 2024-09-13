import cv2

def apply_speckle_filter(image):
    return cv2.medianBlur(image, 5)

def load_images(before_vv_path, before_vh_path, after_vv_path, after_vh_path):
    # Load VV and VH images for before and after datasets
    before_vv = cv2.imread(before_vv_path, cv2.IMREAD_GRAYSCALE)
    before_vh = cv2.imread(before_vh_path, cv2.IMREAD_GRAYSCALE)
    
    after_vv = cv2.imread(after_vv_path, cv2.IMREAD_GRAYSCALE)
    after_vh = cv2.imread(after_vh_path, cv2.IMREAD_GRAYSCALE)

    # Apply speckle filtering to both VV and VH images
    before_vv = apply_speckle_filter(before_vv)
    before_vh = apply_speckle_filter(before_vh)
    
    after_vv = apply_speckle_filter(after_vv)
    after_vh = apply_speckle_filter(after_vh)

    # Stack VV and VH as two-channel images for both before and after
    before_combined = cv2.merge([before_vv, before_vh])  # Two channels for before
    after_combined = cv2.merge([after_vv, after_vh])      # Two channels for after

    return before_combined, after_combined
