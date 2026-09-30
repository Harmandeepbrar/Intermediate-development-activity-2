import unittest
from shape.rectangle import Rectangle


class TestInit(unittest.TestCase):
    """Defines tests for  __init__ method."""

    def test_color_is_blank_string(self) -> None:
        # Arrange
        color = " "
        length = 5
        width = 6

        # Act
        with self.assertRaises(ValueError) as context:
            rectangle = Rectangle(color, length, width)

        # Assert
        expected = "color cannot be blank"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_length_is_less_than_zero(self) -> None:
        # Arrange
        color = "red"
        length = -5
        width = 6

        # Act
        with self.assertRaises(ValueError) as context:
            rectangle = Rectangle(color, length, width)

        # Assert
        expected = "length must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_width_is_less_than_zero(self) -> None:
        # Arrange
        color = "red"
        length = 5
        width = -6

        # Act
        with self.assertRaises(ValueError) as context:
            rectangle = Rectangle(color, length, width)

        # Assert
        expected = "width must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_initialize_new_instance(self) -> None:
        # Arrange
        color = "red"
        length = 5
        width = 6

        # Act
        rectangle = Rectangle(color, length, width)

        # Assert (used name mangling )
        self.assertEqual("red", rectangle._Shape__color)
        self.assertEqual(5, rectangle._Rectangle__length)
        self.assertEqual(6, rectangle._Rectangle__width)
        
        
class TestColorProperty(unittest.TestCase):
    """Tests for the color property."""

    def test_returns_current_state(self) -> None:
        # Arrange
        rectangle = Rectangle("red", 5, 6)

        # Act
        actual = rectangle.color

        # Assert
        expected = "red"
        self.assertEqual(expected, actual)
        
class TestAreaProperty(unittest.TestCase):
    """Tests for the area property."""

    def test_returns_area_of_rectangle(self) -> None:
        # Arrange
        rectangle = Rectangle("red", 5, 6)

        # Act
        actual = rectangle.area

        # Assert
        expected = 30
        self.assertEqual(expected, actual)
        
class TestGetPerimeter(unittest.TestCase):
    """Tests for the get_perimeter method."""

    def test_returns_perimeter_of_rectangle(self) -> None:
        # Arrange
        rectangle = Rectangle("red", 5, 6)

        # Act
        actual = rectangle.get_perimeter()

        # Assert
        expected = 22
        self.assertEqual(expected, actual)
        
class TestStr(unittest.TestCase):
    """Tests for the __str__ method."""

    def test_returns_string_representation(self) -> None:
        # Arrange
        rectangle = Rectangle("red", 5, 6)

        # Act
        actual = rectangle.__str__()

        # Assert
        expected = ("The shape color is red.\n"
                    "This rectangle has a length of 5cm and a width of 6cm.")
        self.assertEqual(expected, actual)
