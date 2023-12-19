#!/usr/bin/python3
""" Task (Advanced) 9. Compare 2 squares """


class Square:
    """
    This class represents a square.

    Attributes:
        size (float or int): The size of the square.
    """
    def __init__(self, size=0):
        """Initializes a square with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The size to set.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Equality comparison based on the square area."""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Inequality comparison based on the square area."""
        return (self.area() != other.area())

    def __lt__(self, other):
        """Less than comparison based on the square area."""
        return (self.area() < other.area())

    def __le__(self, other):
        """Less than or equal comparison based on the square area."""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """Greater than comparison based on the square area."""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Greater than or equal comparison based on the square area."""
        return (self.area() >= other.area())
