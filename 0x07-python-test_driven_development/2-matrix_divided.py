#!/usr/bin/python3
"""
Module for matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
    - matrix (list of lists): Matrix to be divided.
    - div (number): Number to divide all matrix elements by.

    Returns:
    - list of lists: New matrix with elements divided by div,
    rounded to 2 decimal places.

    Raises:
    - TypeError: If matrix is not a list of lists of integers or floats.
    - TypeError: If each row of the matrix does not have the same size.
    - TypeError: If div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
