import tkinter as tk
from Geometry.point import Point
from Geometry.line import Line
class TKpanel(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.lines = []

    def add_line(self, p1,p2: Point):
        self.lines.append(Line(p1,p2))
        self.draw()

    def draw(self):
        self.delete("all")
        for line in self.lines:
            self.create_line(line.start_point.x, line.start_point.y, line.end_point.x, line.end_point.y, fill="red", width=2)
