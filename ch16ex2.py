"""Write a __eq__ method for the Line class so two lines are considered equal if:

    They connect equivalent points,

    in either order (start-to-end or end-to-start)"""
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
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        return ((self.p1 == other.p1 and self.p2 == other.p2) or
                (self.p1 == other.p2 and self.p2 == other.p1))


#test
start1 = Point(0, 0)
start2 = Point(0, 0)
end = Point(200, 100)

line_a = Line(start1, end)
line_b = Line(start2, end)
line_c = Line(end, start1)
line_d = Line(start1, start2)

print(line_a == line_b)  # True
print(line_a == line_c)  # True
print(line_b == line_c)  # True
print(line_a == line_d)  # False
