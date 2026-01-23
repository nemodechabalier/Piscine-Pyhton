from typing import Any


def callLimit(limit: int):
    """
    Decorator factory that limits the number of times a function can be called.

    Args:
        limit: Maximum number of times the decorated function can be called

    Returns:
        A decorator function (callLimiter)
    """
    count = 0

    def callLimiter(function):
        """
        Decorator that wraps a function to limit its calls.

        Args:
            function: The function to be decorated

        Returns:
            A wrapped function (limit_function) that enforces the call limit
        """

        def limit_function(*args: Any, **kwds: Any):
            """
            Wrapper function that executes the original function
            if limit not exceeded.

            Args:
                *args: Positional arguments to pass to the original function
                **kwds: Keyword arguments to pass to the original function

            Returns:
                The result of the original function if limit not exceeded,
                 None otherwise
            """
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
