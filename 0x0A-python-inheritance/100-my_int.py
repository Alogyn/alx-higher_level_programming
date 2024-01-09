#!/usr/bin/python3
'''
Module for MyInt class, __eq__ function & __ne__ function.
'''


class MyInt(int):
    """Class MyInt that inherits from int.

    MyInt is a rebel. MyInt has == and != operators inverted.
    """

    def __eq__(self, other):
        """Overrides the == operator.

        Args:
            other (int): The other integer for comparison.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator.

        Args:
            other (int): The other integer for comparison.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
