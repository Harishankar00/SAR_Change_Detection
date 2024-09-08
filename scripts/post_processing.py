import cv2
import numpy as np
import geopandas as gpd
from skimage.measure import label, regionprops
from shapely.geometry import Polygon

def post_process_change_map(change_map, min_area=50):
    # Label connected components
    labeled_map = label(change_map)
    
    # Filter out small changes (noise)
    filtered_map = np.zeros_like(change_map)
    for region in regionprops(labeled_map):
        if region.area >= min_area:  # Keep only significant changes
            for coord in region.coords:
                filtered_map[coord[0], coord[1]] = 1
                
    return filtered_map

def vectorize_change_map(change_map):
    # Convert the change map to vector polygons (GeoJSON)
    contours, _ = cv2.findContours(change_map.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    polygons = [Polygon(c.squeeze()) for c in contours if len(c) >= 3]  # Create polygons from contours
    gdf = gpd.GeoDataFrame(geometry=polygons)
    
    gdf.to_file("results/change_polygons.geojson", driver="GeoJSON")
    print("Vectorization complete!")

if __name__ == "__main__":
    # Load the change map
    change_map = np.load('results/change_map.npy')
    
    # Post-process the change map
    filtered_map = post_process_change_map(change_map)
    
    # Convert to vector polygons and save as GeoJSON
    vectorize_change_map(filtered_map)
