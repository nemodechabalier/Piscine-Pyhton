import numpy as np
import os
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image and display its format and pixel content in RGB.

    Args:
        path: Path to the image file

    Returns:
        NumPy array containing the image pixels in RGB format

    Raises:
        TypeError: If path is not a string
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file format is not supported
    """
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    if not path.lower().endswith(('.jpg', '.jpeg')):
        raise ValueError("Only accept jpg and jpeg")
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    try:
        img = Image.open(path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        array = np.array(img)
        print(f"The shape of image is: {array.shape}")
        return array

    except Exception as e:
        raise ValueError(f"Error loading image: {e}")
