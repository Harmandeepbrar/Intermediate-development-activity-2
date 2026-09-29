"""Provides the Shape abstract."""
__author__ = "Harmandeep Brar"
__version__ = "1.0.0"
from abc import ABC, abstractmethod


class Shape(ABC):
    """Represents a shape."""

    def __init__(self, color: str):
        """Initialize new Shape instance.

        Args:
            color: The color of the shape.

        Raises:
            ValueError: If color is a blank string.
        """
        color = color.strip()
        if color == "":
            raise ValueError("color cannot be blank")
        self.__color = color

    @property
    def color(self) -> str:
        """Gives the color of the shape.

        Returns:
            str: The color of the shape.
        """
        return self.__color

    @abstractmethod
    def area(self) -> float:
        """Gives the area of the shape.

        Returns:
            float: The area of the shape.
        """