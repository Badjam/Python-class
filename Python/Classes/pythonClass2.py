

class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
        
square = Polygon(4, "Square")
pentagon = Polygon(5, "Pintagon")

print(square.name)
print(square.sides)

print(pentagon.sides)
print(pentagon.name)