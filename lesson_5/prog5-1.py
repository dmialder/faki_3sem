class Shape:

    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
        pass

class Triangle(Shape):
    
    def set_area(self):
        self.ar = self.hight * self.width / 2
    
    def get_area(self):
        return self.ar


class Rectangle(Shape):

    def set_area(self):
        self.ar = self.hight * self.width
    
    def get_area(self):
        return self.ar

hight = 5
width = 8

triangle = Triangle(hight, width)
rectangle = Rectangle(hight, width)
triangle.set_area()
rectangle.set_area()

print(f"triangle with {hight} hight and {width} width, area is: {triangle.get_area()}")
print(f"rectangle with {hight} hight and {width} width, area is: {rectangle.get_area()}")