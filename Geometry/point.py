class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        self._y = value

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# a=Point(8, 4)
# print(a.x)
#print(a)  # Output: Point(8, 4)
#b=Point(78,9)
#print(b)  # Output: Point(78, 9)