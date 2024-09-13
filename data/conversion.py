import os
from PIL import Image
from multiprocessing import Pool

def convert_image(image_info):
    input_dir, output_dir, filename = image_info
    png_path = os.path.join(input_dir, filename)
    tif_path = os.path.join(output_dir, filename.replace('.png', '.tif'))

    with Image.open(png_path) as img:
        img = img.convert('RGB')  # Convert to RGB if needed
        img.save(tif_path, 'TIFF')
    
    return f"Converted {filename} to {tif_path}"

def batch_convert_png_to_tif(input_dir, output_dir, num_workers=4):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Prepare image information for multiprocessing
    image_info = [(input_dir, output_dir, filename) for filename in os.listdir(input_dir) if filename.endswith('.png')]

    # Use multiprocessing to process images in parallel
    with Pool(num_workers) as p:
        results = p.map(convert_image, image_info)
    
    for result in results:
        print(result)

# The main block to prevent issues on Windows
if __name__ == '__main__':
    input_directory = r'D:\SAR_Change_Detection\data\image_before_pre\dataset_sar_vv'
    output_directory = r'D:\SAR_Change_Detection\data\image_before_pre\dataset_sar_vv'
    
    batch_convert_png_to_tif(input_directory, output_directory, num_workers=8)
