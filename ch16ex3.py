"""Write a midpoint method for the Line class that:

    Calculates the midpoint of the line segment.

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

    def midpoint(self):
        x = (self.p1.x + self.p2.x) / 2
        y = (self.p1.y + self.p2.y) / 2
        return Point(x, y)

start = Point(0, 0)
end1 = Point(300, 0)
end2 = Point(0, 150)
line1 = Line(start, end1)
line2 = Line(start, end2)

mid1 = line1.midpoint()
print(mid1)  # Should be Point(150.0, 0.0)

mid2 = line2.midpoint()
print(mid2)  # Should be Point(0.0, 75.0)

line3 = Line(mid1, mid2)
print(line3)  # Optional, just to check it creates the line
