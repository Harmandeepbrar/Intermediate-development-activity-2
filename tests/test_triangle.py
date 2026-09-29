import unittest
from shape.triangle import Triangle


class TestInit(unittest.TestCase):
    """Define tests for the __init__ method."""

    def test_color_is_blank_string(self) -> None:
        # Arrange
        color = "   "
        side_1 = 5
        side_2 = 6
        side_3 = 7

        # Act
        with self.assertRaises(ValueError) as context:
            triangle = Triangle(color, side_1, side_2, side_3)

        # Assert
        expected = "color cannot be blank"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_side_1_less_than_zero(self) -> None:
        # Arrange
        color = "red"
        side_1 = -1
        side_2 = 6
        side_3 = 7

        # Act
        with self.assertRaises(ValueError) as context:
            triangle = Triangle(color, side_1, side_2, side_3)

        # Assert
        expected = "side_1 must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_side_2_less_than_zero(self) -> None:
        # Arrange
        color = "red"
        side_1 = 5
        side_2 = -1
        side_3 = 7

        # Act
        with self.assertRaises(ValueError) as context:
            triangle = Triangle(color, side_1, side_2, side_3)

        # Assert
        expected = "side_2 must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_side_3_less_than_zero(self) -> None:
        # Arrange
        color = "red"
        side_1 = 5
        side_2 = 6
        side_3 = -1

        # Act
        with self.assertRaises(ValueError) as context:
            triangle = Triangle(color, side_1, side_2, side_3)

        # Assert
        expected = "side_3 must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_sides_do_not_satisfy_triangle_inequality_theorem(self) -> None:
        # Arrange
        color = "red"
        side_1 = 1
        side_2 = 1
        side_3 = 10

        # Act
        with self.assertRaises(ValueError) as context:
            triangle = Triangle(color, side_1, side_2, side_3)

        # Assert
        expected = "The sides do not satisfy the Triangle Inequality Theorem"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_initialize_new_instance(self) -> None:
        # Arrange
        color = "red"
        side_1 = 5
        side_2 = 6
        side_3 = 7

        # Act
        triangle = Triangle(color, side_1, side_2, side_3)

        # Assert (uses name mangling)
        self.assertEqual("red", triangle._Shape__color)
        self.assertEqual(5, triangle._Triangle__side_1)
        self.assertEqual(6, triangle._Triangle__side_2)
        self.assertEqual(7, triangle._Triangle__side_3)
        
class TestColorProperty(unittest.TestCase):
    """Tests for the color property."""
    def test_returns_current_state(self) -> None:
        # Arrange
        triangle = Triangle("red", 5, 6, 7)

        # Act
        actual = triangle.color

        # Assert
        expected = "red"
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()