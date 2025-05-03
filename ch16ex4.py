"""Write a midpoint method for the Rectangle class that:

    Finds the center point of the rectangle.

    Returns it as a Point object."""

class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        """Initialize the Point with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self):
        """Return a nicely formatted string representing the Point."""
        return f'Point({self.x}, {self.y})'

class Line:
    """represents a line segment between two points"""

    def __init__(self, p1, p2):
        """initializes two point objects"""
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        """formats string representing the line"""
        return f'Line({self.p1}, {self.p2})'

class Rectangle:
    """represents a rectangle.
    Attributes: width, height, corner (Point).
    """
    def __init__(self, width, height, corner):
        """initializes rectangle with width, height, and corner"""
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self):
        """return a nicely formatted string representing the rectangle"""
        return f'Rectangle({self.width}, {self.height}, {self.corner})'

    def midpoint(self):
        x = self.corner.x + self.width / 2
        y = self.corner.y + self.height / 2
        return Point(x, y)

#test
corner = Point(30, 20)
rectangle = Rectangle(100, 80, corner)

mid = rectangle.midpoint()
print(mid)  # Should be Point(80.0, 60.0)

diagonal = Line(corner, mid)
print(diagonal)
