from html import parser
import tkinter as tk
from Geometry.line import Line
from Geometry.point import Point
from canvas import TKpanel
from Geometry.pen import Pen
from Class import Turtle
from commands import Command
from command_parser import Parser
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Drawing Application")

        self.canvas = TKpanel(self.root, width=1100, height=1100, bg="white")
        self.canvas.pack()
        
    def run(self):    

        pen = Pen(self.canvas, "blue", "Parker",x=550, y=550)
        #pen.move_to(200, 200)   # moves pen to (200,200), no drawing yet
        #pen.line_to(300, 200)   # draws line from (200,200) → (300,200)
        #pen.line_to(300, 300)   # draws line from (300,200) → (300,300)
        #pen.line_to(200, 300)   # draws line from (300,300) → (200,300)
        #pen.line_to(200, 200)   # draws line back to start, closing square
        cmd=Command(Turtle, pen)
        #cmd.create_square()

    # give commands one at a time
        Result=input("Enter Direction (F/+/-) or for create square press 1: ")
        angle = input("Enter angle for the shape: ")
        direction = Parser(pen, step=50, angle=angle)
        if Result == "1":
            cmd.create_square()
        else:

            direction.run(Result, angle)
        print("Completed")
        self.root.mainloop()
    
