from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(img: np.ndarray, x: int = 400, y: int = 100,
         width: int = 450, height: int = 400) -> np.ndarray:
    """
    Zoom on a specific region of the image.

    Args:
        img: Original image array
        x: Starting x coordinate (default: 400)
        y: Starting y coordinate (default: 100)
        width: Width of the region (default: 450)
        height: Height of the region (default: 400)

    Returns:
        Zoomed image array
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("it must be the np.ndarray")
    zoomed = img[y:y+height, x:x+width]
    print(f"New shape after slicing: {zoomed.shape}")
    return zoomed


def gray(img: np.ndarray) -> np.ndarray:
    """
    Convert image to grayscale using luminosity method.
    Formula: 0.299*R + 0.587*G + 0.114*B

    Args:
        img: Color image array

    Returns:
        Grayscale image array
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("it must be the np.ndarray")
    gray = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gray_value = (0.299 * img[i, j, 0] +
                          0.587 * img[i, j, 1] +
                          0.114 * img[i, j, 2]).astype(np.uint8)
            gray[i, j, 0] = gray_value
            gray[i, j, 1] = gray_value
            gray[i, j, 2] = gray_value

    return gray


def main():
    """
    Load image zoom on it put it in gray and display it
    """
    img = ft_load("animal.jpeg")
    print(img)
    zoomed = zoom(img, x=450, y=100, width=400, height=400)
    print(zoomed)
    img_gray = gray(zoomed)

    plt.imshow(img_gray)
    plt.title("Zoomed Image")
    plt.show()


if __name__ == "__main__":
    main()
