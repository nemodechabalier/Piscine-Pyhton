import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and print its shape before and after slicing.

    Args:
        family: 2D list to slice
        start: Starting index
        end: Ending index

    Returns:
        Sliced 2D list
    """
    if not isinstance(family, list):
        raise TypeError("Family must be a list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be int")
    if len(family) == 0:
        raise ValueError("Family list can be empty")

    try:
        array = np.array(family)
    except Exception as e:
        raise ValueError(f"Cannot convert to numpy array: {e}")

    if array.ndim != 2:
        raise ValueError("Family must be a 2D array")

    print(f"My shape is : {array.shape}")

    sliced_array = array[start:end]

    print(f"My new shape is : {sliced_array.shape}")

    return sliced_array.tolist()
