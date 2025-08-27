from Class import Turtle
from Geometry.pen import Pen

class Parser:
    def __init__(self, pen: Pen, step=10, angle=90):
        # make turtle with pen
        self.turtle = Turtle(direction=0, angle=angle, pen=pen)
        self.pen = pen
        self.step = step  # default step size

    def rasta(self, command: str):
        match command:
            case "F":
                self.turtle.move_forward(self.step)
            case "+":
                self.turtle.turn_left()
            case "-":
                self.turtle.turn_right()
            case _:
                print(f"Unknown command: {command}")
    def run(self, commands: str, angle: float):
        for cmd in commands:
            self.rasta(cmd)
