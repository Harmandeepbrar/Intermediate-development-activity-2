"""A program to demonstrate the concepts from module 2."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

from shape import *

def main():
    """The main entry point for the program.""" 

    # 1. Create an empty list that will later store Shape objects.
    shapes = []


    # 2. Code a statement which creates an instance of the Triangle 
    # class.
    # Append the Triangle to the list of shapes.
    triangle = Triangle("red", 5, 6, 7)
    shapes.append(triangle)

    # 3. Code a statement which creates an instance of the Rectangle 
    # class.
    # Append the Rectangle to the list of shapes.
    rectangle = Rectangle("red", 1, 5)
    shapes.append(rectangle)

    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    rectangle = Rectangle("green", 4 ,4 )
    shapes.append(rectangle)
    
    rectangle = Rectangle("blue", 4 ,4 )
    shapes.append(rectangle)

    triangle = Triangle("yellow", 5, 2 ,4 )
    shapes.append(triangle)

    # 5. Iterate through the list of Shapes. On each iteration:
    #    - Print the shape.
    #    - Print the area of the shape to 2 decimal places.
    #    - Print the perimeter of the shape to 2 decimal places.
    for shape in shapes:
        print(shape)
        print(f"Area: {shape.area:.2f}")
        print(f"Perimeter: {shape.get_perimeter():.2f}")


if __name__ == "__main__":
    main()
