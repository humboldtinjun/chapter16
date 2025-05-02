import turtle


class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: float, y: float):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__temp = temp
        self.__x = x
        self.__y = y
        self.__t = turtle.Turtle()
        self.__t.color("yellow")
        self.__t.shape("circle")
        self.__t.goto(self.__x, self.__y)
        

    def get_mass(self):
        return self.__mass

    def get_x_pos(self):
        return self.__x

    def get_y_pos(self):
        return self.__y

    def __str__(self):
        return f"Sun(name={self.__name}, mass={self.__mass}, x=({self.__x}, y={self.__y}, temp={self.__temp})"
