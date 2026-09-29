"""Provide the Triangle class."""

__author__ = "Harmandeep Brar"
__version__ = "1.0.0"
from shape.shape import Shape
from math import sqrt

class Triangle(Shape):
    """Represents a geometric shape formed by connecting three points 
       not in a straight line by straight line segments."""

    def __init__(self, color: str, side_1: float, side_2: float, side_3: float):
        """Initializes a new Triangle instance.

        Args:
            color: The color of the triangle.
            side_1: The length of the first side of triangle in centimeters.
            side_2: The length of the second side of triangle in centimeters.
            side_3: The length of the third side of triangle in centimeters.

        Raises:
            ValueError: If color is blank, if any side is less than or equal to zero or 
            If the three sides do not satisfy the requirements of the Triangle Inequality Theorem.
        """
        super().__init__(color)

        if side_1 <= 0:
            raise ValueError("side_1 must be a value greater than zero")

        if side_2 <= 0:
            raise ValueError("side_2 must be a value greater than zero")

        if side_3 <= 0:
            raise ValueError("side_3 must be a value greater than zero")

        if (side_1 + side_2 <= side_3
                or side_1 + side_3 <= side_2
                or side_2 + side_3 <= side_1):
            raise ValueError(
                "The sides do not satisfy the Triangle Inequality Theorem")

        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3
        
    @property
    def area(self) -> float:
        """Gives the area of the triangle.

        Returns:
            float: The area of the triangle.
        """
        sp = (self.__side_1 + self.__side_2 + self.__side_3)/ 2
        return sqrt(sp * (sp - self.__side_1) * (sp - self.__side_2) * (sp - self.__side_3))

    def get_perimeter(self) -> float:
        """Gives the perimeter of triangle.

        Returns:
            float: The perimeter of triangle.
        """
        return self.__side_1 + self.__side_2 + self.__side_3

    def __str__(self) -> str:
        """Returns informal string representation of triangle.

        Returns:
            str: The informal string representation of triangle.
        """
        return (f"{super().__str__()}\n"
                f"This triangle has three sides with lengths of {self.__side_1}, {self.__side_2}, and {self.__side_3} centimeters.")