"""models/square.py"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

"""10-main.py"""

#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
