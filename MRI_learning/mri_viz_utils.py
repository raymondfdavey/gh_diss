# Import all the necessary packages
import numpy as np
import nibabel as nib
import itk
import itkwidgets
from ipywidgets import interact, interactive, IntSlider, ToggleButtons
import matplotlib.pyplot as plt
import seaborn as sns


def viz_single_slice(image_path, layer):
    image_obj = nib.load(image_path)
    # Extract data as numpy ndarray
    image_data = image_obj.get_fdata()
    print('image_data pixels data type: ',  image_data.dtype)
    print('image_data type: ',  type(image_data))
    print('image_obj type: ',  type(image_obj))
    height, width, depth = image_data.shape
    print(f"({height}, {width}, {depth})")
    print(f"Plotting Layer {layer} of Image")
    
    plt.figure(figsize=(3, 3))
    plt.imshow(image_data[:, :, layer], cmap='gray')
    plt.title(f"{image_path}\nLayer: {layer}")
    plt.axis('off')
    plt.show()
    
def explore_3dimage(image_data, layer, image_path):
    plt.figure(figsize=(10, 5))
    plt.imshow(image_data[:, :, layer], cmap='gray');
    plt.title(f'{image_path[2:-7]}', fontsize=20)
    plt.axis('off')
    return layer

def viz_interactive_3D_image(image_path):
    image_obj = nib.load(image_path)
    image_data = image_obj.get_fdata()
    print('image_data pixels data type: ',  image_data.dtype)
    print('image_data type: ',  type(image_data))
    print('image_obj type: ',  type(image_obj))
    height, width, depth = image_data.shape
    print(f"({height}, {width}, {depth})")
    interact(lambda layer: explore_3dimage(image_data, layer, image_path), layer=(0, image_data.shape[2] - 1))
