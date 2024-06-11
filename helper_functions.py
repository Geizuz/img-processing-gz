import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread

def pltimg(image_data):
    imgplot = plt.imshow(image_data)
    plt.show()
    return None

def dim_list():
    inputs = [1,2]
    return [[x, y] for x in inputs for y in inputs]
    
# Output: [[1, 1], [1, 2], [2, 1], [2, 2]]

def custom_dim_list(inputs_list):
    return [[x, y] for x in inputs_list for y in inputs_list]
    
def format1(axis_value, overlap_ratio):
    segment_value = axis_value//2 + int(axis_value*overlap_ratio)
    return slice(0, segment_value)
    
def format2(axis_value, overlap_ratio):
    segment_value = axis_value//2 - int(axis_value*overlap_ratio)
    return slice(segment_value, axis_value)
    
def save_images(image_list, image_path):
		image_label = image_path.split('.')
		for count, image in enumerate(image_list, start = 1):
			plt.imsave(f'{image_label[0]}_{count}.png',image)
				
def square_array(grid_array):
    rows, cols = grid_array.shape[:2]
    if rows == cols:
        return grid_array
    
    min_dim = min(rows, cols)
    
    start_row = (rows - min_dim) // 2
    start_col = (cols - min_dim) // 2

    # Crop the array to the central square region
    square_array = grid_array[start_row:start_row + min_dim, start_col:start_col + min_dim]
    return square_array

#array inset currently designed to work with square aspect ratios
def array_inset(inset, dim_list):
    size = int(inset.shape[0]*2)
    target_height, target_width = size, size
    larger_array = np.zeros((target_height, target_width, 4), dtype = np.uint8)
    
    # Ensure the position is valid
    if (dim_list[0] + inset.shape[0] > target_height or 
        dim_list[1] + inset.shape[1] > target_width):
        raise ValueError("The small array does not fit at the given position in the larger array")
    rgb_inset = (inset*255).astype(np.uint8)
    larger_array[dim_list[0]:dim_list[0] + inset.shape[0],
        dim_list[1]:dim_list[1] + inset.shape[1]] = rgb_inset
    
    return larger_array

def image_segmentation(image_path, overlap_ratio):
    image_ = imread(image_path)
    image = square_array(image_)
    function_map = {
        1: format1,
        2: format2
        }
    image_list = []
    dimension_input_list = dim_list()
    height, width = image.shape[:2]
    
    for input_val in dimension_input_list:
        new_img = image[function_map[input_val[0]](height, overlap_ratio),function_map[input_val[1]](width, overlap_ratio)]
        image_list.append(new_img.copy(order='C'))
    return image_list