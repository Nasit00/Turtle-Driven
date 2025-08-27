from Class import Turtle
from Geometry.pen import Pen
class Command:
    def __init__(self, Turtle, pen:Pen):
        self.turtle = Turtle
        self.pen = pen

    def create_square(self):
        t = Turtle(self.pen)
        t.move_to(500, 500)   # pen ko start point pe le gya
        t.move_forward(200)   # 100px forward draw karega
        t.turn_left()         # 90 degree left
        t.move_forward(200)    # ab upar ki taraf 50px line draw
        t.turn_left()        # back to east
        t.move_forward(200)
        t.turn_left()
        t.move_forward(200) 
