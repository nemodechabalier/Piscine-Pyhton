def square(x: int | float) -> int | float:
    """
    Returns the square of x.

    Args:
        x: A number (int or float) to be squared

    Returns:
        The square of x (x * x)

    Raises:
        TypeError: If x is not an int or float
    """
    if not isinstance(x, (int, float)):
        raise TypeError("must be a int or float")
    return x * x


def pow(x: int | float) -> int | float:
    """
    Returns x raised to the power of itself.

    Args:
        x: A number (int or float) to be exponentiated by itself

    Returns:
        x raised to the power of x (x ** x)

    Raises:
        TypeError: If x is not an int or float
    """
    if not isinstance(x, (int, float)):
        raise TypeError("must be a int or float")
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Creates a closure that applies a function repeatedly to its result.

    Args:
        x: Initial value (int or float)
        function: A function to apply to x

    Returns:
        A callable object (inner function) that applies the function
        to the previous result on each call
    """
    count = x

    def inner() -> float:
        """
        Applies the function to the stored value and updates it.

        Returns:
            The result of applying the function to the current value
        """
        nonlocal count
        count = function(count)
        return count
    return inner
