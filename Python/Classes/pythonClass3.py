
import turtle

class Polygon:
    def __init__(self, sides, name, size, color = "black", line_thickness=5):
        self.sides = sides
        self.name = name
        self.size = size
        self.interior_angles = (self.sides -2)*180
        self.angle = self.interior_angles/self.sides
        self.color = color
        self.line_thickness = line_thickness
        
    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        turtle.done()

square = Polygon(4, "Square", 10)
pentagon = Polygon(5, "Pintagon", 100)


print(square.sides)
print(square.name)

print(square.interior_angles)
print(square.angle)

print(pentagon.name)
print(pentagon.sides)

# square.draw()

# pentagon.draw()

hexagon = Polygon(6, "Hexagon", 100, color="red", line_thickness=20)

hexagon.draw()