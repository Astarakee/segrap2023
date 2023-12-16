

def windowing_intensity(img_array, min_bound, max_bound):
    
    img_array[img_array>max_bound] = max_bound
    img_array[img_array<min_bound] = min_bound
    return img_array