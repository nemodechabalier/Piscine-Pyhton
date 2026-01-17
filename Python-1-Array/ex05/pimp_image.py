import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the colors of the image.
    Allowed operators: =, +, -, *

    Args:
        array: Image array in RGB format

    Returns:
        Inverted image array
    """
    inverted = 255 - array
    plt.imshow(inverted)
    plt.title("inverted Image")
    plt.show()
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Apply red filter (keep only red channel).
    Allowed operators: =, *

    Args:
        array: Image array in RGB format

    Returns:
        Red filtered image array
    """
    red = array.copy()
    red[:, :, 1] = red[:, :, 1] * 0
    red[:, :, 2] = red[:, :, 2] * 0
    plt.imshow(red)
    plt.title("red Image")
    plt.show()
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Apply green filter (keep only green channel).
    Allowed operators: =, -

    Args:
        array: Image array in RGB format

    Returns:
        Green filtered image array
    """
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    plt.imshow(green)
    plt.title("green Image")
    plt.show()
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Apply blue filter (keep only blue channel).
    Allowed operators: =

    Args:
        array: Image array in RGB format

    Returns:
        Blue filtered image array
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    plt.imshow(blue)
    plt.title("blue Image")
    plt.show()
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert image to greyscale using average method.
    Allowed operators: =, /

    Args:
        array: Image array in RGB format

    Returns:
        Greyscale image array
    """
    grey = array.copy()
    grey_value = (array[:, :, 0] / 3 + array[:, :, 1] / 3 +
                  array[:, :, 2] / 3).astype(np.uint8)
    grey[:, :, 0] = grey_value
    grey[:, :, 1] = grey_value
    grey[:, :, 2] = grey_value
    plt.imshow(grey)
    plt.title("grey Image")
    plt.show()
    return grey
