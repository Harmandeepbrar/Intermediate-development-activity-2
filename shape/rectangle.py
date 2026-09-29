"""Gives Rectangle class."""

__author__ = "Harmandeep Brar"
__version__ = "1.0.0"

from shape.shape import Shape


class Rectangle(Shape):
    """Represents a geometric shape that has four sides with four right angles."""

    def __init__(self, color: str, length: float, width: float):
        """Initializes a new Rectangle.

        Args:
            color: Represents the color of the rectangle.
            length: Represents the length of two opposing sides of the rectangle in centimeters.
            width: Represents the width of two opposing sides of the rectangle in centimeters.

        Raises:
            ValueError: If color is blank or if length or width is less than or equal to zero.
        """

        super().__init__(color)
        if length <= 0:
            raise ValueError("length must be a value greater than zero")

        if width <= 0:
            raise ValueError("width must be a value greater than zero")
        self.__length = length
        self.__width = width

    @property
    def area(self) -> float:
        """Return the area of the rectangle.
        
        Returns:
            float: The area of the rectangle.
        """
        return self.__length * self.__width
