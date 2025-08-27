from .point import Point
class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return f"Line(start={self.start_point}, end={self.end_point})"

    def length(self):
        return ((self.end_point.x - self.start_point.x) ** 2 + (self.end_point.y - self.start_point.y) ** 2) ** 0.5
#a=Line(Point(1, 2), Point(4, 6))
#print(a)  # Output: Line(start=Point(1, 2), end=Point(4, 6))
#print(a.length())  # Output: 5.0