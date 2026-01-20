class calculator:
    """A calculator class that performs operations on vectors with scalars"""

    def __init__(self, vector: list):
        """Initialize the calculator with a vector

        Args:
            vector (list): A list of numbers (int or float)
        """
        if not isinstance(vector, list):
            raise TypeError("must be a list of int or float")
        for v in vector:
            if not isinstance(v, (int, float)):
                raise TypeError("must be a list of int")
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector

        Args:
            object (int): The scalar to add
        """
        if not isinstance(object, int):
            raise TypeError("must be a int")
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] + object
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element of the vector by a scalar

        Args:
            object (int): The scalar to multiply by
        """
        if not isinstance(object, int):
            raise TypeError("must be a int")
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] * object
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element of the vector

        Args:
            object (int): The scalar to subtract
        """
        if not isinstance(object, int):
            raise TypeError("must be a int")
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] - object
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each element of the vector by a scalar

        Args:
            object (int): The scalar to divide by

        Raises:
            ValueError: If division by zero is attempted
        """
        if not isinstance(object, int):
            raise TypeError("must be a int")
        if (object == 0):
            raise ValueError("Division by 0")
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] / object
        print(self.vector)
