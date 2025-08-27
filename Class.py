import math
from Geometry.pen import Pen

class Turtle:
    def __init__(self, pen: Pen, direction=0, angle=90):
        self.pen = pen
        self.direction = float(direction)  # in degrees
        self.angle = float(angle)

    def move_forward(self, distance):
        # calculate dx, dy using trigonometry
        rad = math.radians(self.direction)
        dx = math.cos(rad) * distance
        dy = math.sin(rad) * distance
        new_x = self.pen.x + dx
        new_y = self.pen.y - dy  # subtract dy because Tkinter y grows downward
        self.pen.line_to(new_x, new_y)

    def turn_left(self):
        self.direction += self.angle

    def turn_right(self):
        self.direction -= self.angle

    def move_to(self, x, y):
        # move pen without drawing
        self.pen.move_to(x, y)
