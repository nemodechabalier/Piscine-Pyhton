from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing King Joffrey, a Baratheon-Lannister hybrid"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a King character"""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Get the eye color"""
        return self.eyes

    def get_hairs(self):
        """Get the hair color"""
        return self.hairs

    def set_eyes(self, color: str):
        """Set the eye color"""
        self.eyes = color

    def set_hairs(self, color: str):
        """Set the hair color"""
        self.hairs = color
