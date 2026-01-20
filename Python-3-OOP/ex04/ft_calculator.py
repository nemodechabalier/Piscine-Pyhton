class calculator:
    """A calculator class for vector operations"""

    def __init__(self):
        """Initialize calculator"""
        pass

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise TypeError("V1 and V2 must be list")
        if len(V1) != len(V2):
            raise ValueError("V1 and V2 must have the same dimension")
        for i in range(len(V1)):
            if not isinstance(V1[i], (float, int)) or \
               not isinstance(V2[i], (float, int)):
                raise TypeError("all element in V must be float or int")
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors and print the result"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise TypeError("V1 and V2 must be list")
        if len(V1) != len(V2):
            raise ValueError("V1 and V2 must have the same dimension")
        for i in range(len(V1)):
            if not isinstance(V1[i], (float, int)) or \
               not isinstance(V2[i], (float, int)):
                raise TypeError("all element in V must be float")
        V3 = []
        for i in range(len(V1)):
            V3.append(float(V1[i] + V2[i]))
        print(f"Add Vector is : {V3}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors and print the result"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise TypeError("V1 and V2 must be list")
        if len(V1) != len(V2):
            raise ValueError("V1 and V2 must have the same dimension")
        for i in range(len(V1)):
            if not isinstance(V1[i], (float, int)) or \
               not isinstance(V2[i], (float, int)):
                raise TypeError("all element in V must be float")
        V3 = []
        for i in range(len(V1)):
            V3.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is: {V3}")
