"""Write a make_cross method for the Rectangle class that:

    Uses make_lines() to get the four sides (as Line objects).

    Computes the midpoints of the four sides.

    Makes two new Line objects:

        One connecting the horizontal midpoints (left-to-right).

        One connecting the vertical midpoints (top-to-bottom).

    Returns these two Line objects in a list."""

class Point:
    """represents a point in 2-D space."""

    def __init__(self, x, y):
        """initialize the Point with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self):
        """return a nicely formatted string representing the Point."""
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def translated(self, dx=0, dy=0):
        return Point(self.x + dx, self.y + dy)


class Line:
    """represents a line segment between two points."""

    def __init__(self, p1, p2):
        """initializes two Point objects."""
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        """formats string representing the line."""
        return f'Line({self.p1}, {self.p2})'

    def midpoint(self):
        x = (self.p1.x + self.p2.x) / 2
        y = (self.p1.y + self.p2.y) / 2
        return Point(x, y)


class Rectangle:
    """represents a rectangle.
    Attributes: width, height, corner (Point).
    """

    def __init__(self, width, height, corner):
        """initializes rectangle with width, height, and corner."""
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self):
        """returns a nicely formatted string representing the rectangle."""
        return f'Rectangle({self.width}, {self.height}, {self.corner})'

    def make_points(self):
        """returns the four corner points of the rectangle."""
        p1 = self.corner
        p2 = p1.translated(self.width, 0)
        p3 = p2.translated(0, self.height)
        p4 = p3.translated(-self.width, 0)
        return p1, p2, p3, p4

    def make_lines(self):
        """returns the four side lines of the rectangle."""
        p1, p2, p3, p4 = self.make_points()
        return Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)

    def midpoint(self):
        """finds the center point of the rectangle."""
        x = self.corner.x + self.width / 2
        y = self.corner.y + self.height / 2
        return Point(x, y)

    def make_cross(self):
        """creates two lines crossing through the rectangles center."""
        lines = self.make_lines()
        midpoints = [line.midpoint() for line in lines]
        # Order: top, right, bottom, left

        horiz = Line(midpoints[3], midpoints[1])  # left to right
        vert = Line(midpoints[0], midpoints[2])   # top to bottom

        return [horiz, vert]


# test
# Create a rectangle
corner = Point(30, 20)
rectangle = Rectangle(100, 80, corner)


cross_lines = rectangle.make_cross()


print("Horizontal cross line:", cross_lines[0])
print("Vertical cross line:", cross_lines[1])
