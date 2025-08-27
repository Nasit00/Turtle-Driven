from .point import Point
class Pen:
    def __init__(self,canvas, color, brand,x,y):
        self.canvas = canvas
        self.color = color
        self.brand = brand
        self.x = x
        self.y = y

    def __str__(self):
        return f"Pen(color={self.color}, brand={self.brand})"

    def write(self, text):
        return f"{self.color} {self.brand} pen writes: {text}"
    
    def move_to(self, x, y):
        self.x = x
        self.y = y
    
    def line_to(self, x, y):
        self.canvas.create_line(self.x, self.y, x, y, fill="Red")
        self.x = x
        self.y = y
    
    def Current_Position(self,Cp):
        self.Cp=Cp
        return f"Current position of {self.color} {self.brand} pen is: {self.Cp}"
    def get_position(self):
        return self.Current_Position(self.Cp)

#a=Pen("blue", "Bic")
#print(a)  # Output: Pen(color=blue, brand=Bic)
#print(a.write("Hello, World!"))  # Output: blue Bic pen writes: Hello, World!
#print(a.move_to(10, 20))  # Output: blue Bic pen moves to: (10, 20)
#print(a.line_to(30, 40))  # Output: blue Bic pen draws line to: (30, 40)
#print(a.Current_Position(Point(10,20)))
#a.Current_Position(Point(10, 20))
#print(a.get_position())  # Output: Current position of blue Bic pen is: Point(10, 20)
