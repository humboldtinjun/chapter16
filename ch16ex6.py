"""Write a Circle class with:

    Attributes:

        center → a Point object

        radius → a number

    Special methods:

        __init__ → initialize the circle

        __str__ → return a readable string

    A method:

        draw() → use turtle graphics to draw the circle"""


import turtle
import math

class Point:
    """represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def translated(self, dx=0, dy=0):
        return Point(self.x + dx, self.y + dy)


class Line:
    """represents a line segment between two points."""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'

    def midpoint(self):
        x = (self.p1.x + self.p2.x) / 2
        y = (self.p1.y + self.p2.y) / 2
        return Point(x, y)


class Rectangle:
    """represents a rectangle with width, height, and a corner Point."""

    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self):
        return f'Rectangle({self.width}, {self.height}, {self.corner})'

    def make_points(self):
        p1 = self.corner
        p2 = p1.translated(self.width, 0)
        p3 = p2.translated(0, self.height)
        p4 = p3.translated(-self.width, 0)
        return p1, p2, p3, p4

    def make_lines(self):
        p1, p2, p3, p4 = self.make_points()
        return Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)

    def midpoint(self):
        x = self.corner.x + self.width / 2
        y = self.corner.y + self.height / 2
        return Point(x, y)

    def make_cross(self):
        lines = self.make_lines()
        midpoints = [line.midpoint() for line in lines]
        horiz = Line(midpoints[3], midpoints[1])
        vert = Line(midpoints[0], midpoints[2])
        return [horiz, vert]


class Circle:
    """represents a circle with a center Point and radius."""

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f'Circle({self.center}, {self.radius})'

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)

        t.penup()
        t.goto(self.center.x + self.radius, self.center.y)
        t.setheading(90)
        t.pendown()

        circumference = 2 * math.pi * self.radius
        n = 60  # number of segments
        length = circumference / n
        angle = 360 / n

        t.left(angle / 2)
        for _ in range(n):
            t.forward(length)
            t.left(angle)


def draw_rectangle(rect):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    p1, p2, p3, p4 = rect.make_points()
    t.penup()
    t.goto(p1.x, p1.y)
    t.pendown()
    t.goto(p2.x, p2.y)
    t.goto(p3.x, p3.y)
    t.goto(p4.x, p4.y)
    t.goto(p1.x, p1.y)

#test
corner = Point(20, 20)
rectangle = Rectangle(100, 100, corner)

center = rectangle.midpoint()
radius = rectangle.height / 2

circle = Circle(center, radius)
print(circle)  # Should print Circle(Point(70.0, 70.0), 50.0)

draw_rectangle(rectangle)
circle.draw()

turtle.done()
