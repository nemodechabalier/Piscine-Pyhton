from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize character with a first name and alive status

        Args:
            first_name (str): The first name of the character
            is_alive (bool): Whether the character is alive (default: True)
        """
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to change the health state of the character"""
        pass


class Stark(Character):
    """A class representing a member of House Stark"""

    def die(self):
        """Change the health state of the character to dead"""
        self.is_alive = False
