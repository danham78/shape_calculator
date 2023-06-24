class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        self.picture = ''
        for i in range(self.height):
            self.picture += '*' * self.width + '\n'
        if self.width > 50 or self.height > 50:
            return f'Too big for picture.'
        else:
            return self.picture
        
    def get_amount_inside(self, shape):
        self.shape = shape
        amount_horiz = self.width // self.shape.width
        amount_vert = self.height // self.shape.height
        return amount_horiz * amount_vert
    
class Square(Rectangle):

    def __str__(self):
        return f'Square(side={self.side})'

    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width
        self.side = width

    def set_height(self, height):
        self.width = height
        self.height = height
'''
rect = Rectangle(8, 16)
print(rect)
print(rect.get_area())
print(rect.get_perimiter())
print(rect.get_diagonal())
print(rect.get_picture())
rect_2 = Rectangle(4, 4)
print(rect_2)
print(rect_2.get_area())
print(rect_2.get_perimiter())
print(rect_2.get_diagonal())
print(rect_2.get_picture())
print(rect.get_amount_inside(rect_2))
'''
rect = Rectangle(6, 3)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
print(rect.get_diagonal())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
