#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square with size validation."""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): size of the square (must be >= 0)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
